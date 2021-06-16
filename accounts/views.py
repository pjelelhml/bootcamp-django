from django.contrib.auth import authenticate, login as login, logout
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.post or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username,
                            password=password)
        if user != None:
            # user is valid and active -> is_active
            # request.user == User
            login(request, user)
            return redirect("/")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1
    return render(request, "forms.html", {"form": form})


def logout_view(request):
    logout(request)
    # request.user == Anon User
    return redirect("/login")
