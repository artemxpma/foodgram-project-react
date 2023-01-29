from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# User = get_user_model()


class User(AbstractUser):
    """Custom user model."""
    email = models.EmailField(
        'email address',
        max_length=254,
        unique=True,
    )
    first_name = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Invalid First Name',
            )
        ]
    )
    second_name = models.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='Invalid Second Name',
            )
        ]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


class Subscribtion(models.Model):
    """User subscription model."""
    user = models.ForeignKey(
        User,
        related_name='subscriber',
        verbose_name='Subscriber',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='author',
        verbose_name='Author',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            UniqueConstraint(fields=['user', 'author'],
                             name='unique_subscription')
        ]
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'


# from django.contrib.auth.models import AbstractUser  # , UserManager
# from django.core.validators import RegexValidator
# from .utils import check_input
# class User(AbstractUser):
#     """Custom user model."""
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
#     first_name = models.CharField(
#         max_length=150,
#         validators=[
#             RegexValidator(
#                 regex=r'^[\w.@+-]+$',
#                 message='Invalid Username',
#             )
#         ]
#     )
#     second_name = models.CharField(
#         max_length=150,
#         validators=[
#             RegexValidator(
#                 regex=r'^[\w.@+-]+$',
#                 message='Invalid Username',
#             )
#         ]
#     )

#     REQUIRED_FIELDS = ['email', 'username', 'first_name', 'last_name']

#     @property
#     def is_admin(self):
#         return self.role == User.ADMIN
