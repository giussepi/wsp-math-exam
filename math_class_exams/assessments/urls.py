# -*- coding: utf-8 -*-
""" assessments' urls """

from django.urls import path

from . import views


app_name = "assessments"

urlpatterns = [
    path("", views.AssessmentList.as_view(), name='assessment_list'),
    path("<int:pk>/", views.AssessmentDetail.as_view(), name='assessment_detail'),
    path("new_assessment/<int:pk>/", views.TakeAssessment.as_view(), name='assessment_take'),
]
