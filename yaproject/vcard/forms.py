from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from yaproject.vcard.models import VCard


class MemberAccountForm(ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'maxlength': 75}),
        label=('Email address'))
    password = forms.CharField(widget=forms.PasswordInput,
        label='Your Password')

    class Meta:
        model = User
        exclude = ('first_name', 'last_name', 'groups', 'user_permissions',
            'is_staff', 'is_active', 'is_superuser',
            'last_login', 'date_joined')

    def clean_email(self):
        data = self.cleaned_data['email']

        if User.objects.filter(email__exact=data).exists():
            raise forms.ValidationError("change email")

        return data


class VCardForm(ModelForm):
    class Meta:
        model = VCard