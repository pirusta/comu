from django.contrib import admin

from .models import Word, UserWord

class WordAdmin(admin.ModelAdmin):
    model = Word
    list_display = ['word', 'usage_order']

admin.site.register(Word, WordAdmin)
admin.site.register(UserWord)
