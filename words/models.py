from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=30,unique=True)
    usage_order = models.IntegerField(default=0)

class UserWord(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='word',
	on_delete=models.DO_NOTHING
    )
    default_word = models.OneToOneField(
        Word,
	blank = True,
	null = True,
        related_name='default_word',
	on_delete=models.DO_NOTHING
    )
    is_custom_word = models.BooleanField(
        default=False,
        verbose_name='Is User added word',
    )
    word = models.CharField(max_length=30,unique=True,blank=True,null=True)
    usage_count =  models.IntegerField(default=1)
