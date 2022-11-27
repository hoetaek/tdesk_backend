from django.contrib import admin
from .models import Wordsearch

@admin.register(Wordsearch)
class WordsearchAdmin(admin.ModelAdmin):
    pass
