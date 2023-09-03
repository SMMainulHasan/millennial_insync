from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import UserInfo


class UserRegistrationForm(UserCreationForm):
    editor = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','editor', 'password1', 'password2']

    def save(self, commit= True):
        user_obj = super().save(commit = False)

        if commit == True:
            user_obj.save()
            is_editor = self.cleaned_data.get('editor')

            UserInfo.objects.create(
                user = user_obj,
                editor = is_editor
            )
        return user_obj