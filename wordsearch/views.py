from rest_framework import viewsets

from wordsearch.serializers import WordsearchSerializer
from .models import Wordsearch


class WordsearchViewset(viewsets.ViewSet):
    queryset = Wordsearch.objects.all()
    serializer_class = WordsearchSerializer
