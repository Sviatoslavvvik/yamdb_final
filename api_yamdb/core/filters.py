from django_filters import CharFilter, FilterSet, ModelChoiceFilter

from reviews.models import Categories, Genres, Title


class TitlesFilter(FilterSet):
    category = ModelChoiceFilter(field_name="category",
                                 to_field_name='slug',
                                 queryset=Categories.objects.all())
    genre = ModelChoiceFilter(field_name="genre",
                              to_field_name='slug',
                              queryset=Genres.objects.all())
    name = CharFilter(lookup_expr='contains')

    class Meta:
        model = Title
        fields = ('year',)
