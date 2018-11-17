from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from diary.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """記事管理画面"""
    pass

