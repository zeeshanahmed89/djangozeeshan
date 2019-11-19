from django.db import models

# Create your models here.

class login(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=30)

class python(models.Model):
    Sesion = models.CharField(max_length=40)


    def __str__(self):
        return self.session


class student(models.Model):
    name = models.CharField(max_length=40,unique=False)
    Session = models.ForeignKey("Python",on_delete=models.PROTECT)

