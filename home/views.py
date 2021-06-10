from django.shortcuts import render,  redirect, get_object_or_404
from django.core.paginator import InvalidPage, Paginator, EmptyPage, PageNotAnInteger
from .models import BlogModel 
# from taggit.models import Tag
# from .forms import PostForm
from django.db.models import Q
from django.contrib import messages
# from .forms import CommentForm




# Create your views here.






# def blog_detail(request, slug): 
#     post=Post.objects.filter(slug=slug).first()
#     comments= BlogComment.objects.filter(post=post)
#     context={'post':post, 'comments': comments, 'user': request.user}
#     return render(request, "blog/blogPost.html", context)




def blog_detail(request , slug):
    context = {}
    # if request.method == 'POST':
    #     cf = CommentForm(request.POST or None)
    #     if cf.is_valid():
    #         content = request.POST.get('content')
    #         comment = Comment.objects.create(post = post, user = request.user, content = content)
    #         comment.save()
    #         return redirect(post.get_absolute_url())
    #     else:
    #         cf = CommentForm()
            
    #     context ={
    #         'comment_form':cf,
    #     }
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request , 'blog_detail.html' , context)



# def post_detail(request, post):
#     post=get_object_or_404(BlogModel,slug=post,)
#     try:
#         blog_obj = BlogModel.objects.filter(slug = post).first()
#         # context['blog_obj'] =  blog_obj
#     except Exception as e:
#         print(e)

#     # post=BlogModel.objects.filter(slug=slug).first()
#     # List of active comments for this post
#     comments = blog_obj.comments.filter(active=True)
#     new_comment = None
#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.blog_obj = blog_obj
#             # Save the comment to the database
#             new_comment.save()
#             # redirect to same page and focus on that comment
#             return redirect(blog_obj.get_absolute_url()+'#'+str(new_comment.id))
#         else:
#             comment_form = CommentForm()
#     context={'blog_obj':blog_obj, 'comments': comments,'comment_form':comment_form}  
#     return render(request , 'blog_detail.html' , context)



# def post_detail(request, post):
#     post=BlogModel.objects.filter(slug=post).first()

#     # List of active comments for this post
#     comments = Comment.objects.filter(post=post)
#     new_comment = None

#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#             # redirect to same page and focus on that comment
#             return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
#         else:
#             comment_form = CommentForm()

#     return render(request, 'blog_detail.html',{'post':post,'comments': comments,'comment_form':comment_form})

# def reply_page(request):
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             post_id = request.POST.get('post_id')  # from hidden input
#             parent_id = request.POST.get('parent')  # from hidden input
#             post_url = request.POST.get('post_url')  # from hidden input
#             reply = form.save(commit=False)
    
#             reply.post = BlogModel(id=post_id)
#             reply.parent = Comment(id=parent_id)
#             reply.save()
#             return redirect(post_url+'#'+str(reply.id))
#     return redirect("blogi.html")








   

def index(request):
    # return HttpResponse("This is my home page(/)")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("This is my about page(/about)")
    return render(request, 'about.html')


def skills(request):
    # return HttpResponse("This is my skills page(/skills)")
    return render(request, 'skills.html')


# def blog(request):
#     # return HttpResponse("This is my blog page(/blog)")
#     return render(request, 'blogi.html')

# # def blog(request):
#     context = {'blogs' : BlogModel.objects.all()}
#     return render(request , 'blogi.html' , context)



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
    # tag = None
    # if tag_slug:
    #     tag = get_object_or_404(Tag, slug=tag_slug)
    #     posts = posts.filter(tags__in=[tag])

    # return render(request , 'blogi.html', {'blogs': posts, page:'pages', 'tag':tag})
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


# def add_comment(request, slug):
#     post = get_object_or_404(BlogModel, slug = slug)
#     # post = BlogModel.objects.filter(slug = slug).first()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('blog:blog_detail', slug = post.slug)

#     else:
#         form = CommentForm()
#     template = 'add_comment.html'
#     context = {'form': form}
#     return render(request,  template, context)


