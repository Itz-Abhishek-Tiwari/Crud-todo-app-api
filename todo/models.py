from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class TodoUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User mush have an email address")
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=30)
    objects = TodoUserManager()
    

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class Todos(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    completed = models.BooleanField()

    def __str__(self):
        return self.title

