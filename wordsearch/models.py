from django.db import models
import io

from wordsearch.helper.difficulty_option import Difficulty, DifficultyOption
from wordsearch.helper.puzzle_data import PuzzleData
from wordsearch.helper.worksheet import Worksheet


class Wordsearch(models.Model):
    class Difficulty(models.TextChoices):
        EASY = "EASY", "쉬움"
        NORMAL = "NORMAL", "보통"
        DIFFICULT = "DIFFICULT", "어려움"

    class Lang(models.TextChoices):
        KR = "KR", "한글"
        EN = "EN", "영어"

    difficulty = models.CharField(
        max_length=10, choices=Difficulty.choices, default=Difficulty.EASY
    )
    is_scramble = models.BooleanField()
    is_uppercase = models.BooleanField()
    lang = models.CharField(max_length=2, choices=Lang.choices, default=Lang.KR)
    words = models.JSONField()

    def __str__(self):
        return str(self.words)

    def generate(self):
        puzzle_data = PuzzleData(
            self.words,
            DifficultyOption(self.difficulty),
            is_uppercase=self.is_uppercase,
            is_hint_twist=self.is_scramble,
        )
        puzzle_data.make()
        worksheet = Worksheet(puzzle_data)
        worksheet.write()
        worksheet.write_answer()
        bio = io.BytesIO()

        worksheet.save(bio)
        bio.seek(0)
        return bio
