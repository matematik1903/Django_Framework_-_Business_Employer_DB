from django.db import models
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=25, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Status user'
        verbose_name_plural = 'Status user'


class Employer(models.Model):
    customer_name = models.CharField(max_length=128, default=None, null=True,blank=True)
    customer_email = models.EmailField(default=None, null=True,blank=True)
    customer_phone = models.CharField(max_length=25,default=None, null=True,blank=True)
    customer_city = models.CharField(max_length=25, default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "User - %s" % self.customer_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Vacancy(models.Model):
    company = models.ForeignKey(Employer, default=None, null=True, blank=True)
    name = models.CharField(max_length=128)
    salary = models.IntegerField(blank=True, null=True, default=None)
    type_salary = models.CharField(blank=True, null=True, default=None, max_length=8)
    description = models.TextField()
    requirements = models.TextField(default=None, null=True)
    duties = models.TextField(default=None, null=True)
    package_that_compensates = models.TextField(default=None, null=True)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    status = models.ForeignKey(Status, default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Vacancy N: %s" % self.name

    class Meta:
        verbose_name = 'Vacancy' # Произносимое имя в однині
        verbose_name_plural = "Vacancys" # Произносимое имя в множині
