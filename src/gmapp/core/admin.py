from django.contrib import admin
from .models import Encounters, User_encounters

# Register your models here.
#TODO register encounters and user_encounters models
@admin.register(Encounters)
class EncountersAdmin(admin.ModelAdmin):
    list_display = ('id', 'translations', 'area')
    search_fields = ('translations', 'area')
    list_filter = ('area',)
    ordering = ('id',)