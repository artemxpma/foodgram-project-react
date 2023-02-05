from django.contrib import admin
from django.contrib.admin import display

from recipes import models


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author', 'in_favourites')
    list_filter = ('author', 'name', 'tags',)
    readonly_fields = ('in_favourites',)

    @display(description='Times added to favourite')
    def in_favourites(self, obj):
        return obj.favourites.count()


@admin.register(models.Ingridient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement')


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


@admin.register(models.IngridientValue)
class IngredientValueAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'value')


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'ingredient')


@admin.register(models.Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
