from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # first_name 				= models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


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
