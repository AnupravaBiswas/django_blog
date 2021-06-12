from django.shortcuts import render,  redirect
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from .models import BlogModel
from .models import CommentModel
from django.db.models import Q
from .forms import CommentForm




# Create your views here.

# def blog_detail(request , slug):
#     context = {}
#     try:
#         blog_obj = BlogModel.objects.filter(slug = slug).first()
#         context['blog_obj'] =  blog_obj
        
#     except Exception as e:
#         print(e)
#     return render(request , 'blog_detail.html' , context)



def index(request):
    # return HttpResponse("This is my home page(/)")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("This is my about page(/about)")
    return render(request, 'about.html')


def skills(request):
    # return HttpResponse("This is my skills page(/skills)")
    return render(request, 'skills.html')


def blog(request):
    
    post_list = BlogModel.objects.all().order_by('-created_at')

    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    # search
    query = request.GET.get("q")
    if query:
        posts=BlogModel.objects.filter(Q(title__icontains=query)).distinct()

    return render(request , 'blogi.html', {'blogs': posts, page:'pages'})


def search(request):
    template ='home/blogi.html'
    query=request.GET.get('q')
    if query:
        results = BlogModel.objects.filter(Q(title__icontains =query  ) | Q(content__icontains= query))
    else:
        results = BlogModel.objects.all()
    pages = Pagination(request, results, num=3)
    context = {
        'items': pages[0],
        'page_range': pages[1],
        'query': query,
    }
    return render(request, template, context)



def contact(request):
    # return HttpResponse("This is my contact page(/contact)")
    return render(request, 'contact.htm')




def blog_detail(request , slug):
    context = {}
   
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        # context['blog_obj'] =  blog_obj
        comments = CommentModel.objects.filter(blog = blog_obj)
    except Exception as e:
        print(e)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Comment = CommentModel(your_name= form.cleaned_data['your_name'],
            # comment_text=form.cleaned_data['comment_text'],
            comment = form.save(commit=False)
            comment.blog = blog_obj
            # blog=blog_obj)
            comment.save()
            return redirect('blog_detail', slug=blog_obj.slug)
    else:
        form = CommentForm()
 
    context = {
            'blog_obj':blog_obj,
            'form':form,
            'comments':comments,
        }
    # return render(request,'blogapp/detailview.html',context)
    return render(request , 'blog_detail.html' , context)
