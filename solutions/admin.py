from django.contrib import admin
from .models import Solution

class SolutionsAdmin(admin.ModelAdmin):
    list_display = ('slug', 'solution', 'clase', 'date', 'link') #Add the field you want to display in the Admin area.

admin.site.register(Solution, SolutionsAdmin)