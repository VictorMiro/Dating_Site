from django import forms
from django.core.exceptions import ValidationError

from datingcore.models import CustomUser, CategoryOFUSER, CityOFUSER


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm your password')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Enter normal password')
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class SearchForm(forms.Form):
    age = forms.IntegerField(initial=18, required=False)
    rating = forms.IntegerField(initial=0, required=False)
    category = forms.ModelChoiceField(queryset=CategoryOFUSER.objects.all(), required=False, empty_label='------')
    gender = forms.ChoiceField(choices=CustomUser.TYPE_CHOICES)
    city = forms.ModelChoiceField(queryset=CityOFUSER.objects.all(), required=False, empty_label='------')

    def search_by_age(self, queryset):
        return queryset.filter(age=self.cleaned_data['age'])

    def search_by_rating(self, queryset):
        return queryset.filter(rating=self.cleaned_data['rating'])

    def search_by_category(self, queryset):
        return queryset.filter(category=self.cleaned_data['category'])

    def search_by_gender(self, queryset):
        return queryset.filter(gender=self.cleaned_data['gender'])

    def search_by_city(self, queryset):
        return queryset.filter(city=self.cleaned_data['city'])

    def get_search_queryset(self, queryset):

        for field_name in self.fields:
            if field_name in self.cleaned_data and self.cleaned_data[field_name]:
                queryset = getattr(self, f"search_by_{field_name}")(queryset)
        return queryset


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('avatar', 'username', 'first_name', 'last_name', 'age', 'category', 'gender', 'city', 'bio', 'phone')
        widgets = {
            'category': forms.widgets.CheckboxSelectMultiple(attrs={}),
            'city': forms.widgets.CheckboxSelectMultiple(attrs={})
        }

    def save(self, *args, **kwargs):
        user = super(EditProfileForm, self).save(commit=False)
        user.save()
        return user

