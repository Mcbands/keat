from django.contrib import admin
from .models import Category, Blog,SocialLink, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title",  "id", "author", "status", "is_featured")
    list_editable = ("is_featured",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, BlogAdmin)

# Register your models here.
admin.site.register(Category)
admin.site.register(SocialLink)
admin.site.register(Comment)
