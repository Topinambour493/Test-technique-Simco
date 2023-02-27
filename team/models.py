from django.conf import settings
from django.db import models


class Team(models.Model):
    "Team object"

    trainer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=100,
    )

    class Meta:
        unique_together = ("trainer", "name")

    def __str__(self):
        return "{} ({})".format(self.name, self.trainer.username)
