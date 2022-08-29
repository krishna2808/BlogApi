from django.contrib import admin
from post.models import Post, Comment
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'user', 'title',  'discription' , 'post_date']
@admin.register(Comment)
class CommetAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment', 'comment_date']


