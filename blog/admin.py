from django.contrib import admin
from .models import Article, Author, Tag

class ArticalAdmin(admin.ModelAdmin):
    pass
admin.site.register(Article, ArticalAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qq', 'addr', 'email')
    list_display_links = ()
    list_filter = ()
#     list_select_related = True
    list_per_page = 10
    list_editable = ()
    search_fields = ('name', 'qq', 'email')
admin.site.register(Author, AuthorAdmin)

class TagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, TagAdmin)
