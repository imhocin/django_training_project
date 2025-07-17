from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import redirect, render
from django_training_project import forms


def login_view(request):

    login_form = forms.LoginForm(request.POST or None)

    if login_form.is_valid():
        username = login_form.cleaned_data["username"]
        password = login_form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            raise forms.ValidationError("Error: user not found")

    context = {"page": "login", "login_form": login_form}

    return render(request, "auth/login.html", context)


User = get_user_model()


def register_view(request):
    register_form = forms.RegisterForm(request.POST or None)

    if register_form.is_valid():
        username = register_form.cleaned_data.get("user_name")
        password = register_form.cleaned_data.get("password")
        email = register_form.cleaned_data.get("email")
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )

    context = {"register_form": register_form}
    return render(request, "auth/register.html", context)


def log_out(request):
    logout(request)
    return redirect("/")
