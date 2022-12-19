# Generated by Django 4.1.4 on 2022-12-16 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restaurantes", "0002_restaurante_delete_task"),
    ]

    operations = [
        migrations.CreateModel(
            name="Voto",
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
                ("pergunta", models.CharField(default="SOME STRING", max_length=200)),
                ("pub_date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Opcao",
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
                ("votes", models.IntegerField(default=0)),
                (
                    "opcao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantes.restaurante",
                    ),
                ),
                (
                    "pergunta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantes.voto",
                    ),
                ),
            ],
        ),
    ]