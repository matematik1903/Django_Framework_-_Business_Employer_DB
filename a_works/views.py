from a_works.models import Vacancy,Employer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse


def get_vacancy_search(request):
    user_info = Vacancy.objects.filter(name__icontains=request.POST['search_login'])

    data = serializers.serialize('json', user_info)
    return HttpResponse(data, content_type='application.json')


def get_city_search(request):
    user_info = Employer.objects.filter(customer_city__icontains=request.POST['search_login'])

    data = serializers.serialize('json', user_info)
    return HttpResponse(data, content_type='application.json')


def vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    return render(request, 'products/product.html', locals())


@login_required()
def vacancy_delete(request, vacancy_id):
    Vacancy.objects.filter(id=vacancy_id).update(is_active=False)
    return HttpResponseRedirect('/Personal_office')