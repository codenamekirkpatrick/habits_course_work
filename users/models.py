from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {"blank": True, "null": True}


# Кастомный менеджер пользователя
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **extra_fields):
        """Создает и возвращает пользователя с email, именем и паролем."""
        if not email:
            raise ValueError("Почта не указана")
        if not first_name:
            raise ValueError("Имя не указано")

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        """Создает и возвращает суперпользователя с email, именем и паролем."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, first_name, password, **extra_fields)


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(verbose_name="Почта", unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=30, unique=True)
    phone = models.IntegerField(
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    telegram_chat_id = models.CharField(
        verbose_name="ID чата Telegram", max_length=100, **NULLABLE
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Имя-{self.first_name}|Почта-{self.email}" f"|Телефон-{self.phone}"
