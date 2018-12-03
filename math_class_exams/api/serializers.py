# -*- coding: utf-8 -*-
""" apis' serializers """

from rest_framework import serializers

from math_class_exams.assessments.models import Assessment, UserAssesment, \
    Question, Solution, Answer


class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assessment
        fields = ('id', 'created', 'name', 'assessments', 'threshold')


class UserAssesmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAssesment
        fields = ('id', 'user', 'assessment', 'score', 'result')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'text', 'difficulty', 'assessment', 'solutions')


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ('id', 'text', 'correct')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'userassesment', 'question', 'selected_answer')
