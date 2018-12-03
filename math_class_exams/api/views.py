# -*- coding: utf-8 -*-
""" apis' views """

from rest_framework import viewsets

from math_class_exams.assessments.models import Assessment, UserAssesment, \
    Question, Solution, Answer

from .serializers import AssessmentSerializer, UserAssesmentSerializer, \
    QuestionSerializer, SolutionSerializer, AnswerSerializer


class AssessmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer


class UserAssesmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserAssesment.objects.all()
    serializer_class = UserAssesmentSerializer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SolutionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
