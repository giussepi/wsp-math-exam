# -*- coding: utf-8 -*-
""" assessments' forms """

import re

from django import forms

from .constants import PassFail
from .models import Assessment, UserAssesment, Answer


class TakeAssessmentForm(forms.ModelForm):
    """ UserAssesment ModelForm """
    class Meta:
        model = Assessment
        fields = ('id', )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        for question in self.instance.question_set.all():
            self.fields['question_{}'.format(question.pk)] = \
                forms.IntegerField()

    def clean(self):
        super().clean()
        question_pattern = re.compile('^question\_(?P<question_id>[\d]+)$')

        question_queryset = self.instance.question_set.all()

        for k, v in self.cleaned_data.items():
            found = question_pattern.match(k)
            if not found:
                raise forms.ValidationError('Invalid field name {}'.format(k))
            if not question_queryset.filter(id=found.group('question_id')):
                raise forms.ValidationError('Invalid question id')
            question = question_queryset.filter(id=found.group('question_id'))[0]
            if not question.solutions.filter(id=v):
                raise forms.ValidationError('Invalid answer id')
            self.cleaned_data[k] = (question, question.solutions.filter(id=v)[0])

        return self.cleaned_data

    def save(self, *args, **kwargs):
        user_assessment = UserAssesment.objects.get_or_create(
            user=self.user, assessment=self.instance)[0]

        for answer in user_assessment.answer_set.all():
            answer.delete()

        for question, solution in self.cleaned_data.values():
            Answer.objects.create(
                userassesment=user_assessment, question=question, selected_answer=solution)

        user_assessment.score = user_assessment.calculate_score()

        if user_assessment.score >= self.instance.threshold:
            user_assessment.result = PassFail.PASSED
        else:
            user_assessment.result = PassFail.FAILED

        user_assessment.save()
