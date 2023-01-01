from django.contrib import admin

import models


@admin.register(models.Ingridient)
class IngridientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


@admin.register(models.Recipy)
class RecipyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


@admin.register(models.IngridientValue)
class IngridientValueAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)


@admin.register(models.Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)

# @admin.register(Genre)
# class GenreAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name', 'slug')
#     search_fields = ('name',)
#     empty_value_display = '-пусто-'


# @admin.register(Title)
# class TitleAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name', 'year',
#                     'description', 'category')
#     search_fields = ('name',)
#     list_filter = ('year',)
#     list_editable = ('category',)
#     empty_value_display = '-пусто-'
