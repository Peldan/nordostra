from django import forms
from django.core.exceptions import ValidationError
from registration.forms import RegistrationForm
from narvaro.models import Person


class PersonForm(forms.ModelForm):
    persons = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())


class ExRegistrationForm(RegistrationForm):
    is_human = forms.ChoiceField(label = "Are you human?:")

