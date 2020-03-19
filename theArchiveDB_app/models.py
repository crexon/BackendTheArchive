from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=25, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=75, unique=True)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.name


class Libro(models.Model):
    title = models.CharField(max_length=25, blank=False)
    author = models.CharField(max_length=20, blank=False)
    rate_average = models.CharField(max_length=50, blank=False)
    publish_date = models.DateField()
    valoration = models.ManyToManyField(Usuario, through='Valoracion', related_name='+')
    estanteria = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title


class Estanteria(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='+')
    book_id = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='+')
    state = models.IntegerField(blank=False)
    puntuation = models.FloatField(blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.state


class Valoracion(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='+')
    book_id = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='+')
    review = models.CharField(max_length=200, blank=False)
    rate = models.IntegerField(blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.review


class Challange(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='+')
    total_book = models.IntegerField(blank=False)
    actual_book = models.IntegerField(blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.total_book


class Update(models.Model):
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='+')
    description = models.IntegerField(blank=False)
    total_votes = models.ManyToManyField(Usuario, related_name='+')
    comment = models.ManyToManyField(Usuario, through="Comment", related_name='+')
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.description


class Comment(models.Model):
    update_id = models.ForeignKey(Update, on_delete=models.CASCADE, related_name='+')
    user_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='+')
    comment = models.CharField(max_length=200, blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.comment
