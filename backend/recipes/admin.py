from django.contrib import admin
from django.contrib.admin import display

from recipes import models


class RecipeIngredientInline(admin.TabularInline):
    model = models.IngredientValue
    min_num = 1


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'in_favorites')
    list_filter = ('author', 'name', 'tags',)
    readonly_fields = ('in_favorites',)
    inlines = (RecipeIngredientInline, )

    @display(description='Times added to favorite')
    def in_favorites(self, obj):
        return obj.favorites.count()


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


@admin.register(models.IngredientValue)
class IngredientValueAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount')


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


@admin.register(models.Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
