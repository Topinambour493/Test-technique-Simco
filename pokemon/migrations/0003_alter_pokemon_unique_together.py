# Generated by Django 3.2.12 on 2023-02-22 08:36
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pokemon", "0002_rename_surname_pokemon_nickname"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="pokemon",
            unique_together={("trainer", "nickname")},
        ),
    ]
