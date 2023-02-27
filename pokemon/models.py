from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError

from pokedex.models import PokedexCreature
from team.models import Team


class Pokemon(models.Model):
    """Pokemon object"""

    pokedex_creature = models.ForeignKey(
        PokedexCreature,
        on_delete=models.CASCADE,
    )

    trainer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    nickname = models.CharField(max_length=100, blank=True, null=True)

    level = models.PositiveSmallIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)

    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ("trainer", "nickname")

    def clean(self):
        """
        Set default nickname to related pokedex creature name
        if no nickname is given
        """
        if self.trainer != self.team.trainer:
            raise ValidationError(
                _("this team is not yours, mind your business"), code="invalid"
            )
        if Pokemon.objects.filter(
            trainer=self.trainer
        ).count() >= 6 and not Pokemon.objects.get(pk=self.pk):
            raise ValidationError(
                _(
                    "This team is complete. It is already composed of 6 pokemons. First remove a pokemon from your team if you want to add this one."
                ),
                code="invalid",
            )
        if not self.nickname:
            self.nickname = self.pokedex_creature.name
        self.level = 1 + self.experience // 100
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        """
        Return Pokemon name with the trainer username if it has one

        Return Pokemon name (wild) if not
        """

        return "{} ({})".format(
            self.nickname, self.trainer.username if self.trainer else "wild"
        )

    def receive_xp(self, amount: int) -> None:
        """
        Update pokemon level based on the XP is received
        """
        self.experience += amount
        self.save()
