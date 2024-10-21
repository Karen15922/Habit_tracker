# Generated by Django 5.1.2 on 2024-10-19 10:41

import datetime

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Привычка")),
                ("place", models.CharField(max_length=100, verbose_name="Место")),
                (
                    "time",
                    models.TimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Время выполнения привычки",
                    ),
                ),
                ("action", models.CharField(max_length=100, verbose_name="Действие")),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=True, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "period",
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[django.core.validators.MaxValueValidator(7)],
                        verbose_name="Периодичность привычки",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "time_to_action",
                    models.DurationField(
                        default=datetime.timedelta(seconds=120),
                        verbose_name="Продолжительность выполнения привычки",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="habit",
                        to="habits.habit",
                        verbose_name="Связанная приятная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
