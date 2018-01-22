from django.contrib import admin
from .models import *

class CourseAdmin (admin.ModelAdmin):
        # list_display = ["name", "email"]   # какие поля виводять
        list_display = [field.name for field in users_job._meta.fields]     # вивести всі поля
        exclude = ["name"] # какие поля не виводить при переходе на обэкт ,
                           # на странице редактирование записей
        fields = ["email"] # какие поля виводить при переходе на обэкт ,
                           # на странице редактирование записей
        list_filter = ['name'] # фильтер по полю
        search_fields = ["name"] # поле пошуку по тегу

        class Meta:
            model = users_job


admin.site.register(users_job, CourseAdmin)
