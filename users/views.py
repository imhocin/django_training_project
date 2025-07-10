from django.shortcuts import render
from django.contrib.auth import authenticate
from django_training_project import forms


def login_view(request):

    login_form = forms.LoginForm(request.POST or None)



    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']




    context = {
        'page' : 'login',
        'login_form': login_form,
    }

    return render(request, 'auth/login.html', context)
