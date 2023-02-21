from django.db import models
from django.utils.text import slugify
from django.db.models import UniqueConstraint

from colorfield.fields import ColorField

from users.models import User


class Ingredient(models.Model):
    """Model for Ingredient entity."""
    name = models.CharField(max_length=64)
    slug = models.SlugField(
        editable=False,
        blank=False
    )
    measurement_unit = models.TextField(max_length=64)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
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
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientValue',
        db_index=True,
        related_name='recipes',
        verbose_name='Ingredients'
    )
    tags = models.ManyToManyField(
        Tag,
        db_index=True,
        related_name='recipes',
        verbose_name='Tags'
    )
    time = models.PositiveIntegerField(
        'Cooking time',
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


class IngredientValue(models.Model):
    """Model for value of each ingredient in recipe entity."""
    ingredient = models.ForeignKey(
        Ingredient,
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
        blank=False,
    )

    class Meta:
        verbose_name = 'Ingredient Value in Recipe'
        verbose_name_plural = 'Ingredients Values in Recipes'

    def __str__(self):
        return (
            f'{self.ingredient.name} ({self.ingredient.measurement})'
            f' - {self.value} '
        )


class Favourites(models.Model):
    """Model for Favourites entity."""
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


class Cart(models.Model):
    """Model for Cart entity."""
    user = models.ForeignKey(
        User,
        related_name='cart',
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        related_name='cart',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        constraints = [UniqueConstraint(fields=['user', 'ingredient'],
                                        name='unique_cart')]

    def __str__(self):
        return f'{self.user} added "{self.ingredient}" to his shopping cart'
