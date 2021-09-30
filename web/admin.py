from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    pass
