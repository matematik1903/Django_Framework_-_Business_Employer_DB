from django.conf.urls import url

from login import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.login_fun, name='login'),
    url(r'submit_login/$', views.submit_login, name='submit_login'),
    url(r'logout/$', views.acc_logout, name='acc_logout'),
]