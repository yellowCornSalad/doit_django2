from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from blog.models import Post, Category, Tag

admin.site.register(Post, MarkdownxModelAdmin)
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
