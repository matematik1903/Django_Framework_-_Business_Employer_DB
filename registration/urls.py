from django.conf.urls import url
from registration import views

app_name = 'registration'
urlpatterns = [
    url(r'^$', views.registration, name='registration'),
    url(r'submit_registration/$', views.submit_registration, name='submit_registration'),
]