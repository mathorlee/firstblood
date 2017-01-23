from django.contrib import admin
from .models import Article, Author, Tag

class ArticalAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'score',)
    list_display_links = ()
    list_filter = ()
    list_per_page = 10
    list_editable = ()
    search_fields = ('title',)
admin.site.register(Article, ArticalAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qq', 'addr', 'email',)
    list_display_links = ()
    list_filter = ()
    list_per_page = 10
    list_editable = ()
    search_fields = ('name', 'qq', 'email')
admin.site.register(Author, AuthorAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ()
    list_filter = ()
    list_per_page = 10
    list_editable = ()
    search_fields = ('name',)
admin.site.register(Tag, TagAdmin)
