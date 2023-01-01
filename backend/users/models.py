# from django.contrib.auth.models import AbstractUser, UserManager
# from django.core.validators import RegexValidator
# from django.db import models

# from .utils import check_input


# class CustomUserManager(UserManager):
#     """UserManager для кастомной модели пользователя."""
#     def create_user(self, username, email, password, **extra_fields):
#         """Проверяет данные и создает экземпляр модели пользователя."""
#         check_input(username, email)
#         return super().create_user(
#             username=username, email=email, password=password, **extra_fields)

#     def create_superuser(
#             self, username, email, password, role='admin', **extra_fields):
#         """Проверяет данные и создает экземпляр модели
#         пользователя с правами администратора."""
#         check_input(username, email)
#         return super().create_superuser(
#             username, email, password, role='admin', **extra_fields)


# class User(AbstractUser):
#     """Кастомная модель пользователя."""
#     USER = 'user'
#     ADMIN = 'admin'

#     ROLE_CHOICES = (
#         (USER, 'user'),
#         (ADMIN, 'admin'),
#     )
#     username = models.CharField(
#         db_index=True,
#         max_length=150,
#         unique=True,
#         validators=[
#             RegexValidator(
#                 regex=r'^[\w.@+-]+$',
#                 message='Invalid Username',
#             )
#         ]
#     )
#     role = models.TextField(
#         choices=ROLE_CHOICES,
#         default='user'
#     )
#     bio = models.TextField(
#         'Biography',
#         blank=True,
#         max_length=3000,
#     )
#     objects = CustomUserManager()
#     REQUIRED_FIELDS = ['email']

#     @property
#     def is_admin(self):
#         return self.role == User.ADMIN
