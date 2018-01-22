from a_works.models import Employer, Vacancy, Status
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect


def landing(request):
    return render(request, 'landing/landing.html', locals())


def find(request):                                          # ПОШУК ВАКАНСІЇ
    job_name = request.POST['exampleInputText3']
    city = request.POST['exampleInputText2']

    l_mane = len(job_name)
    i = 0
    flag = 1
    while flag == 1:
        if i == l_mane:
            flag = 0
        elif job_name[i] == " ":
            i = i + 1
        else:
            flag = 0
    job_name = job_name[i:]

    l_mane = len(city)
    i = 0
    flag = 1
    while flag == 1:
        if i == l_mane:
            flag = 0
        elif city[i] == " ":
            i = i + 1
        else:
            flag = 0
    city = city[i:]

    l_mane = len(job_name)
    i = 0
    flag = 1
    k = l_mane - 1
    while flag == 1:
        if i == l_mane:
            flag = 0
        elif job_name[k] == " ":
            k = k - 1
        else:
            flag = 0
    job_name = job_name[:k + 1]

    l_mane = len(city)
    i = 0
    flag = 1
    k = l_mane - 1
    while flag == 1:
        print(k)
        if i == l_mane:
            flag = 0
        elif city[k] == " ":
            k = k - 1
        else:
            flag = 0
    city = city[:k + 1]

    count_job_name = len(job_name)
    count_city = len(city)
    k = "     "

    vacancy = Vacancy.objects.filter(name=job_name, company__customer_city=city, is_active=True, is_main=False)
    if count_job_name < 3:
        vacancy = Vacancy.objects.filter(company__customer_city=city, is_active=True, is_main=False)
    if count_city < 3:
        vacancy = Vacancy.objects.filter(name=job_name, is_active=True, is_main=False)
    if count_city < 3:
        if count_job_name < 3:
            vacancy = Vacancy.objects.filter(is_active=True, is_main=False)
    j = len(vacancy)
    vacancy_main = Vacancy.objects.filter(is_active=True, is_main=True)
    return render(request, 'Job.html', locals())


@login_required()
def add_vacancy(request):
    name = request.user.username
    j_user = Employer.objects.filter(customer_name=name)

    for p in j_user:
        x_company = p

    x_name = request.POST['name']
    x_salary = request.POST['number']
    x_type_salary = request.POST['type_salary']
    x_description = request.POST['comment_1']
    x_requirements = request.POST['comment_2']
    x_duties = request.POST['comment_3']
    x_package_that_compensates = request.POST['comment_4']
    x_status = request.POST['state']

    st = Status.objects.filter(name=x_status)

    for sp in st:
        Vacancy.objects.create(name=x_name, company=p, salary=x_salary, type_salary=x_type_salary,
                               description=x_description, requirements=x_requirements, duties=x_duties,
                               package_that_compensates=x_package_that_compensates, status=sp)
    return HttpResponseRedirect('/Personal_office')


@login_required()
def open_setup(request):
    name = request.user.username
    j_user = Employer.objects.filter(customer_name=name)
    vacancy = Vacancy.objects.filter(company__customer_name=name, is_active=True)

    i = 0
    i = len(vacancy)
    return render(request, 'setting_personal_office.html', locals())


@login_required()
def close_setup(request):
    return HttpResponseRedirect('/Personal_office')


@login_required()
def del_user(request):
    name = request.user.username
    User.objects.filter(username=name).delete()
    job_user = Employer.objects.filter(customer_name=name)
    Vacancy.objects.filter(company=job_user).update(is_active=False)
    Employer.objects.filter(customer_name=name).delete()
    return HttpResponseRedirect('/')


@login_required()
def rename(request):
    phone = request.POST['phone']
    email = request.POST['email']
    name = request.POST['name']
    city = request.POST['city']

    user_name = request.user.username
    User.objects.filter(username=user_name).update(username=name)

    Employer.objects.filter(customer_name=user_name).update(customer_name=name, customer_email=email,
                                                            customer_phone=phone, customer_city=city)
    return HttpResponseRedirect('/Personal_office')


@login_required()
def person(request):
    name = request.user.username
    j_user = Employer.objects.filter(customer_name=name)
    vacancy = Vacancy.objects.filter(company__customer_name=name, is_active=True)

    j = 0
    j = len(vacancy)
    return render(request, 'personal_office.html', locals())
