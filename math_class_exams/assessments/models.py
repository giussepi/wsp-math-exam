# -*- coding: utf-8 -*-
""" assessment's models """

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.urls import reverse

from .constants import QuestionDifficulty


User = get_user_model()


class Assessment(models.Model):
    """ Holds assessments """

    created = models.DateTimeField(auto_now_add=False)
    name = models.CharField(max_length=255)
    assessments = models.ManyToManyField(User, through='UserAssesment')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """ returns the detail url of the object """
        return reverse('assessments:assessment_detail', kwargs={'pk': self.pk})

    def get_score_for_user(self, user):
        """ Returns the score of the user """
        assert isinstance(user, User)

        try:
            obj = user.userassesment_set.get(assessment=self)
        except ObjectDoesNotExist:
            return 0
        else:
            return obj.score


class UserAssesment(models.Model):
    """ Holds User's Assessment scores """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)

    def __str__(self):
        return '{} - {} - {}%'.format(self.user, self.assessment, self.score)

    def calculate_score(self):
        """ """
        total = self.answer_set.count()
        correct_answers = self.answer_set.filter(selected_answer__correct=True).count()

        return (correct_answers * 100) / total


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
