from rest_framework import serializers
from words.models import Word, UserWord 


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word']
