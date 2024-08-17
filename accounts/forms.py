# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    # Optionally, you can override the error messages here:
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.", code='password_mismatch')

        # You can add more custom validation here if needed
        return password2
