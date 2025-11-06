from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator, RegexValidator

from .models import RoomRequest

class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[А-Яа-яЁёs-]+$', 'Введите ФИО кириллицей')]
    )
    email = forms.EmailField(validators=[EmailValidator()])

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2']

class RoomRequestForm(forms.ModelForm):
    class Meta:
        model = RoomRequest
        fields = ['plan_file']
