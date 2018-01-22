from django.contrib import admin
from a_works.models import *


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields] # вивести всі поля
    search_fields = ["name"] # поле пошуку по тегу
    list_filter = ['name']  # фильтер по полю

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class EmployerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employer._meta.fields]
    search_fields = ["customer_name"]
    list_filter = ["customer_name"]  # фильтер по полю

    class Meta:
        model = Employer


admin.site.register(Employer, EmployerAdmin)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ["company", "name", "is_active", "is_main", "salary", "type_salary",  "status", "created", "updated"]
    search_fields = ["company"]
    list_filter = ["name"]  # фильтер по полю

    class Meta:
        model = Vacancy


admin.site.register(Vacancy, VacancyAdmin)