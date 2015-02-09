from django import forms
from django.core.exceptions import ValidationError

from narvaro.models import Person


class PersonForm(forms.ModelForm):
    persons = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())




