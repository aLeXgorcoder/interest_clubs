from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from hobby_categories.models import HobbyCategory


class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('У пользователя должен быть E-mail')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        MALE = 'M', 'Мужчина'
        FEMALE = 'F', 'Женщина'

    email = models.EmailField(unique=True, verbose_name='E-mail')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email_verified = models.BooleanField(default=False, verbose_name='Подтверждение E-mail')
    is_staff = models.BooleanField(default=False, verbose_name='Доступ к панели администратора')
    is_superuser = models.BooleanField(default=False, verbose_name='Администратор')
    is_active = models.BooleanField(default=True, verbose_name='Онлайн')

    age = models.PositiveSmallIntegerField(
        default=18,
        validators=[MinValueValidator(18), MaxValueValidator(100)],
        verbose_name='Возраст'
    )
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE,
        verbose_name='Пол'
    )
    current_category = models.ForeignKey(
        HobbyCategory,
        on_delete=models.PROTECT,
        related_name='current_members',
        verbose_name='Текущая категория',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.age} лет)"

    class Meta:
        ordering = ['first_name']
        indexes = [models.Index(fields=['email'])]
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
