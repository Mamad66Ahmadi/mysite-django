from django.contrib import admin
from blog.models import Post
# Register your models here.

#@admin.register(Post)  (optional, instead of: admin.site.register)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id','title','author','counted_views','status','published_date','created_date')
    list_filter = ('status','author')
    #ordering = ['created_date']
    search_fields = ['title','content']


admin.site.register(Post,PostAdmin)
