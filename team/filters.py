from django_filters import rest_framework as filters

from .models import Team


class TeamFilter(filters.FilterSet):
    """Filters for team listing"""

    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Team
        fields = [
            "name",
        ]
