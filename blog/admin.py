from django.contrib import admin

# Register your models here.
from .models import Article, Author, Tag

admin.site.register([Article, Author, Tag])