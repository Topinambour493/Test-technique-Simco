from rest_framework import serializers

from .models import Team
from pokemon.serializers import PokemonSerializer


class TeamSerializer(serializers.ModelSerializer):
    """Serializer of Team object"""

    trainer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Team
        fields = (
            "id",
            "trainer",
            "name",
        )
        read_only_fields = ("id",)


class TeamDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
        )
