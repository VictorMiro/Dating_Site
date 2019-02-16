from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from django.urls import reverse
from datingcore.forms import RegisterForm


class HomePageView(TemplateView):
    template_name = "homepage.html"


class Register(FormView):
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = 'registration_successfully/'

    def form_valid(self, form):
        form.save()
        return super(Register, self).form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'registration/registration_successfully.html'
