from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from django.urls import reverse
from datingcore.forms import RegisterForm, SearchForm
from datingcore.models import CustomUser


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


class ProfileView(TemplateView):
    template_name = 'profile.html'


class ProfileEditView(UpdateView):
    template_name = 'edit_profile.html'
    model = CustomUser
    fields = ['email']


class SearchFormView(ListView):
    template_name = 'search_form.html'
    model = CustomUser

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(SearchFormView, self).get_context_data(*args, **kwargs)
        if self.request.GET:
            context['form'] = SearchForm(data=self.request.GET)
            if context['form'].is_valid():
                context['customuser_list'] = context['form'].get_search_queryset(context['customuser_list'])
        else:
            context['form'] = SearchForm()
        return context
