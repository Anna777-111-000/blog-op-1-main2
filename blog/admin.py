from django.contrib import admin

# Register your models here.
from .models import Category, Post, Comment, Like, Donation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...


admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Donation)
