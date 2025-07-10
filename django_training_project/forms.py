from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-label',
                'placeholder': 'Full name'
            },
        ),
        label=False,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-label',
            'placeholder': 'Email'
        }),
        label=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control form-label',
            'placeholder': 'Message'
        }),
        label=False,
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-label',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-label',
            }
        )
    )
