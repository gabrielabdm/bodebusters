from django.contrib import admin
from .models import Movie


admin.site.site_header = 'BodeBusters Admin'
admin.site.register(Movie)