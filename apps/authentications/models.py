from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, fio, password=None, **extra_fields):
        if not username:
            raise ValueError('Логин обязателен')
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(username=username ,email=email, fio=fio, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, fio, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username ,email, fio, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, verbose_name="Логин")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email")
    fio = models.CharField(max_length=255, verbose_name="ФИО")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email' ,'fio']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} - {self.email} - {self.fio}'
