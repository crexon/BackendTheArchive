from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from rest_framework.authtoken.models import Token


# Create your models here.

class Libro(models.Model):
    identifier = models.CharField(max_length=150, blank=False)
    title = models.CharField(max_length=150, blank=True)
    authors = models.TextField(blank=True)
    publisher = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    publishedDate = models.CharField(max_length=150, blank=True)
    pageCount = models.CharField(max_length=150, blank=True)
    categories = models.TextField(blank=True)
    thumbnail = models.TextField(blank=True)
    estanteria = models.ManyToManyField(User, through='Estanteria')
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.identifier


class Estanteria(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    book_id = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='+')
    state = models.IntegerField(blank=False)
    progress = models.IntegerField(blank=False)
    recommendation = models.IntegerField(blank=True)
    # recommendation = models.BooleanField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.state


class Valoracion(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    book_id = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='+')
    review = models.CharField(max_length=200, blank=False)
    rate = models.IntegerField(blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.review


class Challange(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    total_book = models.IntegerField(blank=False)
    actual_book = models.IntegerField(blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.total_book


class Update(models.Model):
    username = models.CharField(max_length=200, blank=False)
    type = models.IntegerField(blank=False)
    date = models.DateField(blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.username


class Comment(models.Model):
    update_id = models.ForeignKey(Update, on_delete=models.CASCADE, related_name='+')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    comment = models.CharField(max_length=200, blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.comment
