from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from bureau.models import Redactor


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name", "last_name", "years_of_experience",
        )


class RedactorExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ("username", "first_name", "last_name", "email", "years_of_experience")

    def clean_years_of_experience(self):
        years = self.cleaned_data["years_of_experience"]

        if years < 0:
            raise ValidationError(
                "Ensure that years value is >= 0"
            )

        return years
