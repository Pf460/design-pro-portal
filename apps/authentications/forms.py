from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
import re

User = get_user_model()


class RegisterForm(UserCreationForm):
    agreement = forms.BooleanField(
        required=True,
        label="Согласие на обработку персональных данных",
        error_messages={'required': 'Необходимо согласие на обработку данных.'}
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'fio', 'agreement')

    def clean_fio(self):
        fio = self.cleaned_data.get('fio')
        if not re.match(r'^[А-Яа-яЁё\s\-]+$', fio):
            raise forms.ValidationError("ФИО должно содержать только кириллицу, пробелы и дефис.")
        return fio

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match(r'^[a-zA-Z\-]+$', username):
            raise forms.ValidationError("Логин должен содержать только латиницу и дефис.")
        return username

class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Неверный логин или пароль.",
    }