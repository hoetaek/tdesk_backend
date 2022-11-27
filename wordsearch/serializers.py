from rest_framework import serializers

from wordsearch.models import Wordsearch


class WordsearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wordsearch
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "auth_token",
        )
        read_only_fields = ("auth_token",)
