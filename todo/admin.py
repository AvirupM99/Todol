from django.contrib import admin
from .models import Todomo

# Register your models here.

class Todoadmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todomo, Todoadmin)