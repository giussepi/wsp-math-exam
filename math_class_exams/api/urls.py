# -*- coding: utf-8 -*-
""" api's urls """

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'assessments', views.AssessmentViewSet)
router.register(r'userassessments', views.UserAssesmentViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'solutions', views.SolutionViewSet)
router.register(r'answers', views.AnswerViewSet)

app_name = "api"

urlpatterns = [
    path('', include(router.urls)),
]
