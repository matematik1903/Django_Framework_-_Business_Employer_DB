from django.db import models

class   users_job(models.Model):
     name = models.CharField(max_length=128)
     tell = models.CharField(max_length=128)
     city = models.CharField(max_length=128)
     email = models.EmailField()
     password = models.CharField(max_length=128)

     def __str__(self):
         return "%s - %s" % (self.name, self.email)
         # return self.email          # self - подразумивает запис из етой модели
         # return self.id           # id - номер , создаетса авто
         # return "%s %s" % (self.id, self.email)   # вивести два параметра у відповідності
 # Create your models here.

     class Meta: #
         verbose_name = 'Bohdan' # Произносимое имя в однині
         verbose_name_plural = "Bogdanio" # Произносимое имя в множині