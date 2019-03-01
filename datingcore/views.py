from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView, FormView, ListView
from datingcore.forms import RegisterForm, SearchForm, EditProfileForm
from datingcore.models import CustomUser, Friend


class HomePageView(ListView):
    template_name = "homepage.html"
    model = CustomUser

    def get_queryset(self):
        queryset = self.model.objects.exclude(id=self.request.user.id)[:3]
        return queryset


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
        queryset = self.model.objects.exclude(id=self.request.user.id)
        if self.request.GET:
            self.form = SearchForm(data=self.request.GET)
            self.form.is_valid()
            queryset = self.form.get_search_queryset(queryset)
        else:
            self.form = SearchForm()

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(SearchFormView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
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


class FriendsRelationView(TemplateView):
    template_name = 'Friendlist.html'

    def get(self, request):
        users = CustomUser.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
        args = {'users': users, 'friends': friends}
        return render(request, self.template_name, args)


def change_friends(request, operation, pk):
    friend = CustomUser.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('change_friends')







