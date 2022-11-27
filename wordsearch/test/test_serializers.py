from django.test import TestCase
from ..serializers import WordsearchSerializer
from .factories import WordsearchFactory


class TestWordsearchSerializer(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_wordsearch_serializer(self):
        stub = WordsearchFactory.stub()
        print(stub.difficulty)
