from django.contrib import admin

# Register your models here.

from .models import Files, Courses


admin.site.register(Courses)
admin.site.register(Files)
