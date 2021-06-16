from django.contrib.auth import get_user_model

# check for unique email & username

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "id": "user-password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "id": "user-password"}
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "id": "user-password"}
        )
    )

    # def clean(self):
    #     username = self.cleaned_data.get("username")
    #     password = self.cleaned_data.get("password")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user")
        return username
