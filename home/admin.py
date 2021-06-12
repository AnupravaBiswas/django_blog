from django.contrib import admin

# Register your models here.
from .models import BlogModel,Profile
from .models import CommentModel


admin.site.register(Profile)



# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'status','created_at')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}
# admin.site.register(BlogModel, PostAdmin)
@admin.register(BlogModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user', 'created_at', 'status')
    list_filter = ('status', 'created_at', 'upload_to', 'user')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('user',)
    date_hierarchy = 'created_at'
    ordering = ('status', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('your_name', 'approved')

admin.site.register(CommentModel, CommentAdmin)