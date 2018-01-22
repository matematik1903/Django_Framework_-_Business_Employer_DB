
"""test_project URL Configuration



The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/1.10/topics/http/urls/

Examples:

Function views

    1. Add an import:  from my_app import views

    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')

Class-based views

    1. Add an import:  from other_app.views import Home

    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')

Including another URLconf

    1. Import the include() function: from django.conf.urls import url, include

    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""

from django.conf.urls import url
from django.contrib import admin
from a_works import views


urlpatterns = [
    # url(r'^api/get_employees/', views.get_employees, name='get_employees'),
    url(r'^product/(?P<vacancy_id>\w+)/$', views.vacancy, name='product'),
    url(r'^delete/(?P<vacancy_id>\w+)/$', views.vacancy_delete, name='product_delete'),
    url(r'^get_vacancy_search/$', views.get_vacancy_search, name='get_vacancy_search'),
    url(r'^get_city_search/$', views.get_city_search, name='get_city_search'),
    # url(r'^api/get_drugs/',  views.get_drugs, name='get_drugs'),
]