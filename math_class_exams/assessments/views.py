# -*- coding: utf-8 -*-
""" assessments' views """

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from .forms import TakeAssessmentForm
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


class TakeAssessment(LoginRequiredMixin, TemplateView):
    """ Handles the take assessment view """
    template_name = "assessments/takeassessment_form.html"
    # success_url = reverse_lazy('assessments:assessment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object(kwargs['pk'])

        return context

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Assessment, pk=pk)

    def post(self, request, *args, **kwargs):
        instance = self.get_object(kwargs['pk'])
        form = TakeAssessmentForm(
            request.user, instance=instance, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(instance)

        context = self.get_context_data(**kwargs)
        messages.error(request, 'There were errors validation the form')
        return self.render_to_response(context)
