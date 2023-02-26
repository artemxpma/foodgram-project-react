from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


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

    class Meta:
        ordering = ['id']


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
        ordering = ['-author_id']
        constraints = [
            UniqueConstraint(fields=['user', 'author'],
                             name='unique_subscription')
        ]
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
