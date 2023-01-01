from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

from colorfield.fields import ColorField

from django.contrib.auth import get_user_model
User = get_user_model()
# from users.models import User


class Ingridient(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        editable=False,
        blank=False
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        editable=False,
        blank=False
    )
    color = ColorField(default='#FF0000')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipy(models.Model):
    """Model for Recipy entity."""
    name = models.CharField(
        'Name',
        max_length=128,
        blank=False
    )
    slug = models.SlugField(
        editable=False,
        blank=False
    )
    author = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.CASCADE,
        related_name='recipes',
    )
    image = models.ImageField(
        upload_to='recipes/',
        blank=False
    )
    description = models.TextField(
        max_length=8196,
        blank=False
    )
    ingridients = models.ManyToManyField(
        Ingridient,
        db_index=True,
        related_name='recipes',
    )
    tags = models.ManyToManyField(
        Tag,
        db_index=True,
        related_name='recipes',
    )
    time = models.PositiveIntegerField(
        max_length=3,
        blank=False,
        validators=[
            MaxValueValidator(360),
            MinValueValidator(1)
        ]
    )

    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('article-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)  # can be changed to unique in field


class IgridientValue(models.Model):
    ingridient = models.ForeignKey(
        Ingridient,
        db_index=True,
        on_delete=models.CASCADE
    )
    recipy = models.ForeignKey(
        Recipy,
        db_index=True,
        on_delete=models.CASCADE
    )
    value = models.PositiveIntegerField(
        max_length=3,
        blank=False,
        validators=[
            MaxValueValidator(10000),
            MinValueValidator(1)
        ])
