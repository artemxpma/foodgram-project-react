from django.db import models
from django.utils.text import slugify
from django.db.models import UniqueConstraint

from colorfield.fields import ColorField

# from users.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class Ingridient(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        editable=False,
        blank=False
    )
    measurement = models.TextField(max_length=64)

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
        through='IngridientValue',
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
        verbose_name_plural = "Recipes"


class IngridientValue(models.Model):
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
    )


class Favourites(models.Model):
    user = models.ForeignKey(
        User,
        related_name='favourites',
        on_delete=models.CASCADE
    )
    recipy = models.ForeignKey(
        Recipy,
        related_name='favourites',
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [UniqueConstraint(fields=['user', 'recipy'],  # might be possible to do by unique together
                                        name='unique_favourite')]


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name='cart',
        on_delete=models.CASCADE
    )
    ingridient = models.ForeignKey(
        Ingridient,
        related_name='cart',
        on_delete=models.CASCADE,
    )

    class Meta:
        constraints = [UniqueConstraint(fields=['user', 'ingridient'],
                                        name='unique_favourite')]
