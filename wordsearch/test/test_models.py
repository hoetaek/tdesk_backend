from django.test import TestCase
from .factories import WordsearchFactory


class TestWordsearchModel(TestCase):
    def setUp(self):
        self.wordsearch_factory = WordsearchFactory

    def test_create(self):
        wordsearch = self.wordsearch_factory.create()
        wordsearch.generate()
