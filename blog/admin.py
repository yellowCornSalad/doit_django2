from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from blog.models import Post, Category, Tag, Comment

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Comment)  # 댓글 작성 확인 페이지
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
