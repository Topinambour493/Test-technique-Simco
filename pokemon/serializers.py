from rest_framework import serializers

from .models import Pokemon
from authentication.serializers import UserSerializer
from pokedex.serializers import PokedexCreatureDetailSerializer


class PokemonSerializer(serializers.ModelSerializer):
    """Serializer of Pokemon object"""

    trainer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "pokedex_creature",
            "trainer",
            "nickname",
            "level",
            "experience",
            "team",
        )
        read_only_fields = ("id",)

    def validate(self, attrs):
        """Add pokemon nickname if no nickname is given"""
        nickname = attrs.get("nickname")
        pokedex_creature = attrs.get("pokedex_creature")
        if not nickname:
            attrs["nickname"] = pokedex_creature.name

        return super().validate(attrs)


class PokemonDetailsSerializer(serializers.ModelSerializer):
    pokedex_creature = PokedexCreatureDetailSerializer()

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "nickname",
            "level",
            "experience",
            "pokedex_creature",
            "team",
        )


class PokemonGiveXPSerializer(serializers.Serializer):
    """Serializer of give-xp endpoint"""

    amount = serializers.IntegerField(min_value=0)
