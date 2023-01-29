from django.db import models
from django.utils.text import slugify
from django.db.models import UniqueConstraint

from colorfield.fields import ColorField

from users.models import User


class Ingridient(models.Model):
    """Model for Ingridient entity."""
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        editable=False,
        blank=False
    )
    measurement = models.TextField(max_length=64)

    class Meta:
        verbose_name = 'Ingridient'
        verbose_name_plural = 'Ingridients'
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """Model for Tag entity."""
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        editable=False,
        blank=False
    )
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Model for Recipe entity."""
    name = models.CharField(
        'Name',
        max_length=128,
        blank=False,
        unique=True
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
        verbose_name='Author'
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
        verbose_name='Ingridients'
    )
    tags = models.ManyToManyField(
        Tag,
        db_index=True,
        related_name='recipes',
        verbose_name='Tags'
    )
    time = models.PositiveIntegerField(
        'Cooking time',
        max_length=3,
        blank=False,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class IngridientValue(models.Model):
    ingridient = models.ForeignKey(
        Ingridient,
        db_index=True,
        on_delete=models.CASCADE,
    )
    recipe = models.ForeignKey(
        Recipe,
        db_index=True,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
    )
    value = models.PositiveIntegerField(
        max_length=3,
        blank=False,
    )

    class Meta:
        verbose_name = 'Ingridient Value in Recipe'
        verbose_name_plural = 'Ingridients Values in Recipes'

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement})'
            f' - {self.value} '
        )


class Favourites(models.Model):
    user = models.ForeignKey(
        User,
        related_name='favourites',
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        related_name='favourites',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Favourite'
        verbose_name_plural = 'Favourites'
        constraints = [UniqueConstraint(fields=['user', 'recipe'],
                                        name='unique_favourite')]
        # might be possible to do by unique together


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
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        constraints = [UniqueConstraint(fields=['user', 'ingridient'],
                                        name='unique_cart')]

    def __str__(self):
        return f'{self.user} added "{self.ingridient}" to his shopping cart'
