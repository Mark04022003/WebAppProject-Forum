from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Author

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False  # You want email verification!
        if commit:
            user.save()
        return user

