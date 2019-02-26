from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView, ListView
from django.urls import reverse
from datingcore.forms import RegisterForm, SearchForm, EditProfileForm
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


class SearchFormView(ListView):
    template_name = 'search_form.html'
    model = CustomUser
    paginate_by = 2

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(SearchFormView, self).get_context_data(*args, **kwargs)
        if self.request.GET:
            context['form'] = SearchForm(data=self.request.GET)
            if context['form'].is_valid():
                context['customuser_list'] = context['form'].get_search_queryset(self.object_list)
        else:
            context['form'] = SearchForm()
        return context


class EditUserProfileView(FormView):
    template_name = "edit_profile.html"
    form_class = EditProfileForm

    def form_valid(self, form):
        form.save(user=self.request.user)
        return redirect('success_update')

    def get_form_kwargs(self):
        kwargs = super(EditUserProfileView, self).get_form_kwargs()
        kwargs['instance'] = get_object_or_404(CustomUser, username=self.request.user)
        return kwargs


class SuccessfulEditView(TemplateView):
    template_name = 'successfullEdit.html'

