from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from a_works.models import Employer
from django.http import HttpResponseRedirect
from django.shortcuts import render
import smtplib


def message(request):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")

    msg = "YOUR MESSAGE!"
    server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
    server.quit()
    return HttpResponseRedirect('/')


def registration(request):
    return HttpResponseRedirect('/Personal_office')


def submit_registration(request):
    name = request.POST['name']
    count = User.objects.filter(username=name)
    count = len(count)
    if count > 0:
        error = "Sorry, but such a company is already registered"
        return render(request, "login.html", locals())

    name = request.POST['name']
    l_name = len(name)
    i = 0
    while i < l_name:
        if name[i] == " ":
            error = "Sorry, but the name must not contain spaces"
            return render(request, "login.html", locals())
        i = i + 1

    Employer.objects.create(customer_name=request.POST['name'],
                            customer_phone=request.POST['phone'],
                            customer_email=request.POST['mail'],
                            customer_city=request.POST['city'])

    user = User.objects.create_user(request.POST['name'], request.POST['mail'], request.POST['password'])
    user.save()

    user = authenticate(username=request.POST['name'], password=request.POST['password'])
    login(request, user)
    return HttpResponseRedirect('/Personal_office')
