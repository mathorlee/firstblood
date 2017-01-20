from django.contrib import admin

# Register your models here.
from .models import Person, Blog, Author, Entry
admin.site.register([Person, Blog, Author, Entry])

