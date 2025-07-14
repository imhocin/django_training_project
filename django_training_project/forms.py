from django import forms
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control form-label", "placeholder": "Full name"},
        ),
        label=False,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control form-label", "placeholder": "Email"}
        ),
        label=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control form-label", "placeholder": "Message"}
        ),
        label=False,
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-label",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-label",
            }
        )
    )


User = get_user_model()


class RegisterForm(forms.Form):

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-label",
            }
        )
    )

    user_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-label",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-label",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-label",
            }
        )
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-label",
            }
        )
    )

    def clean_user_name(self):
        username = self.cleaned_data.get("user_name")
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError("this username is tokken")
        return username

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("re_password")
        if password1 != password2:
            raise forms.ValidationError("password is not match!")
        return data
