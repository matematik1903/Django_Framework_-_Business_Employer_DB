from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def login_fun(request):
    return render(request, "login.html", locals())


def submit_login(request):
    user = authenticate(username=request.POST['login'], password=request.POST['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            # ok
        else:
            error = "Вибачте, але ваш акаунт не активний"
            return render(request, "login.html", locals())
            # return HttpResponseRedirect("/login")
    else:
        error = "Sorry, but your account is not registered "
        return render(request, "login.html", locals())
        # return HttpResponseRedirect("/login")
    name = request.POST['login']
    count = User.objects.filter(username=name, is_staff=True)
    _count = len(count)
    if _count > 0:
        return HttpResponseRedirect('/admin')
    return HttpResponseRedirect("/Personal_office")


@login_required()
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
