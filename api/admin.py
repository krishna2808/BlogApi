from django.contrib import admin
from api.models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'name')
    filter_horizontal = ()


# from .models import Post, Comment
# # Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display =  ['id', 'user', 'title', 'discription', 'post_date']


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'post', 'comment', 'comment_date'] 
