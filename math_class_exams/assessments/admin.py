# -*- coding: utf-8 -*-
""" assessments's admin """

from django.contrib import admin


from .models import Assessment, UserAssesment, Question, Solution, Answer


admin.site.register(Assessment)
admin.site.register(UserAssesment)
admin.site.register(Question)
admin.site.register(Solution)
admin.site.register(Answer)
