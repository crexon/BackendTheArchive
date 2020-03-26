from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class Libro(models.Model):
    identifier = models.CharField(max_length=150, blank=False)
    estanteria = models.ManyToManyField(User, through='Estanteria')
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.identifier


class Estanteria(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    book_id = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='+')
    state = models.IntegerField(blank=False)
    recommendation = models.BooleanField(blank=True)
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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    description = models.IntegerField(blank=False)
    total_votes = models.ManyToManyField(User, related_name='+')
    comment = models.ManyToManyField(User, through="Comment", related_name='+')
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.description


class Comment(models.Model):
    update_id = models.ForeignKey(Update, on_delete=models.CASCADE, related_name='+')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    comment = models.CharField(max_length=200, blank=False)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.comment
