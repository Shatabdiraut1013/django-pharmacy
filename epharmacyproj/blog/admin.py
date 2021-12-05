from django.contrib import admin
from .models import Blogpost, Popularpost
# Register your models here.

admin.site.register(Blogpost)
admin.site.register(Popularpost)