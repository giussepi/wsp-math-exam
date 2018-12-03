# -*- coding: utf-8 -*-
""" assessments' views """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView


from .models import Assessment, UserAssesment


class AssessmentList(LoginRequiredMixin, ListView):
    """ handles home page """
    model = Assessment
    template_name = "assessments/assessment_list.html"


class AssessmentDetail(LoginRequiredMixin, DetailView):
    """ Handles the assessment detail view """
    model = Assessment
    template_name = "assessments/assessment_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['score'] = self.object.get_score_for_user(self.request.user)

        return context
