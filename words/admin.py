from django.contrib import admin

from .models import Word, UserWord

admin.site.register(Word)
admin.site.register(UserWord)
