from django_filters.rest_framework import FilterSet, filters

from recipes.models import Ingredient, Recipe, Tag
from users.models import User


class IngredientFilter(filters.SearchFilter):
    search_param = 'name'
    # name = filters.CharFilter(lookup_expr='startswith')

    # class Meta:
    #     model = Ingredient
    #     fields = ['name']


class RecipeFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all(),
    )

    is_favourited = filters.BooleanFilter(method='filter_is_favourited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='filter_is_in_cart')

    class Meta:
        model = Recipe
        fields = ('tags', 'author',)

    def filter_is_favourited(self, queryset, name, value):
        user = self.request.user
        if value and not user.is_anonymous:
            return queryset.filter(favourites__user=user)
        return queryset

    def filter_is_in_cart(self, queryset, name, value):
        user = self.request.user
        if value and not user.is_anonymous:
            return queryset.filter(cart__user=user)
        return queryset
