from factory.django import DjangoModelFactory
from faker import Faker
import re

from .. import models

fake = Faker("ko_KR")


def get_fake_kr_words():
    with open("wordsearch/helper/random_words.txt", "r") as f:
        data = f.read()
        regex_f = r"[가-힣]+"
        search_target_f = data
        data = list(set(re.findall(regex_f, search_target_f)))
    return data


class WordsearchFactory(DjangoModelFactory):
    class Meta:
        model = models.Wordsearch

    difficulty = "EASY"
    """factory.Faker(
        "random_choices", elements=["EASY", "NORMAL", "DIFFICULT"]
    )"""
    is_scramble = fake.pybool()
    lang = "KR"  # factory.Faker("random_choices", elements=["KR", "EN"])
    if lang == "EN":
        words = fake.words(nb=20)
    elif lang == "KR":
        words = fake.words(nb=20, ext_word_list=get_fake_kr_words())
    is_uppercase = fake.pybool() if lang != "KR" else False
