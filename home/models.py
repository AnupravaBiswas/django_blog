# from django.db import models
# from django.contrib.auth.models import User
# from froala_editor.fields import FroalaField
# from .helpers import *


# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

# # Create your models here.
# class BlogModel(models.Model):
#     title = models.CharField(max_length=1000)
#     content = FroalaField()
#     slug = models.SlugField(max_length=1000,null=True, blank=True)
#     image = models.ImageField(upload_to='blog')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.IntegerField(choices=STATUS, default=0)

#     class Meta:
#         ordering = ['-created_at']


#     def __str__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         self.slug = gen_slug(self.title)
#         super(BlogModel, self).save(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
from django.urls import reverse



class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)
    

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class BlogModel(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
    
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    
    # def get_absolute_url(self):
    #     return reverse('blog:blog_detail',args=[self.slug])

 

