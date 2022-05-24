from rest_framework import serializers
from onlinestore.models import *


class BookJournalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'price', 'description', 'created_at']


class BookSerializer(serializers.ModelSerializer):
    class Meta(BookJournalBaseSerializer.Meta):
        model = Book
        fields = BookJournalBaseSerializer.Meta.fields + ['num_pages', 'genre']


class JournalSerializer(serializers.Serializer):
    class Meta(BookJournalBaseSerializer.Meta):
        model = Journal
        fields = BookJournalBaseSerializer.Meta.fields + ['type', 'publisher']
