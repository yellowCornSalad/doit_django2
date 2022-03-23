from django.contrib import admin
from blog.models import Post, Category

admin.site.register(Post)
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
