from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    search_fields = ['author__username', 'post__title', 'text']
    list_display = ['author', 'post', 'text']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('likes', )
    search_fields = ['title', ]


admin.site.register(Tag)
