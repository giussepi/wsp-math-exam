# -*- coding: utf-8 -*-
""" assessments's admin """

from django.contrib import admin


from .models import Assessment, UserAssesment, Question, Solution, Answer


class QuestionInLine(admin.TabularInline):
    """  """
    model = Question
    raw_id_fields = ('solutions', )


class UserAssessmentInLine(admin.TabularInline):
    model = UserAssesment


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    """  """
    inlines = [
        QuestionInLine, UserAssessmentInLine
    ]


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    """  """
    list_display = ('text', 'correct')
    list_display_links = list_display


class SolutionInLine(admin.TabularInline):
    """  """
    model = Question.solutions.through
    max_num = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """  """
    inlines = [
        SolutionInLine
    ]
    exclude = ('solutions', )


admin.site.register(UserAssesment)
admin.site.register(Answer)
