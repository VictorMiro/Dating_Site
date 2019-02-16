from django import forms
from django.contrib.auth.models import User


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

    class Meta:
        model = User
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
