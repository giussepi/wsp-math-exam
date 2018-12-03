# -*- coding: utf-8 -*-
""" assessment's models """

from django.contrib.auth import get_user_model
from django.db import models

from .constants import QuestionDifficulty


User = get_user_model()


class Assessment(models.Model):
    """ Holds assessments """

    created = models.DateTimeField(auto_now_add=False)
    name = models.CharField(max_length=255)
    assessments = models.ManyToManyField(User, through='UserAssesment')

    def __str__(self):
        return str(self.name)


class UserAssesment(models.Model):
    """ Holds User's Assessment scores """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)

    def __str__(self):
        return '{} - {} - {}%'.format(self.user, self.assessment, self.score)


class Question(models.Model):
    """ Hold Assessment's questions """

    text = models.CharField(max_length=255)
    difficulty = models.CharField(
        max_length=1, choices=QuestionDifficulty.CHOICES, default=QuestionDifficulty.EASY)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    solutions = models.ManyToManyField('Solution')

    def __str__(self):
        return '{} - {}'.format(self.assessment, self.difficulty)


class Solution(models.Model):
    """ Holds Questions's solution """

    text = models.TextField()
    correct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.text[:10])


class Answer(models.Model):
    """ Holds UserAssesment's answers """

    userassesment = models.ForeignKey(UserAssesment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Solution, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {}'.format(
            self.userassesment.pk, self.question.pk, self.selected_answer.pk)
