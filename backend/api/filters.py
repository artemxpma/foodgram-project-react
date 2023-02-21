from django_filters.rest_framework import FilterSet, filters

from recipes.models import Recipe, Tag, Ingredient


class IngredientFilter(FilterSet):
    """Custom filter for Ingredient model."""
    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    """Custom filter for Recipe model."""
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
            return queryset.filter(shopping_cart__user=user)
        return queryset
