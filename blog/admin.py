from django.contrib import admin

from blog.models import Post , Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'author' , 'status', 'published_date', 'created_date', 'updated_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_filter = ('status',)
    # ordering = ('-created_date',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name')
    search_fields = ('name',)
    empty_value_display = '-empty-'
    list_filter = ('name',)
    # ordering = ('-created_date',)

