# Generated by Django 5.0.4 on 2024-05-02 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statsApp', '0002_buyurtmataom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buyurtma',
            options={'verbose_name': 'Buyurtma', 'verbose_name_plural': 'Buyurtmalar'},
        ),
        migrations.AlterModelOptions(
            name='buyurtmaichimlik',
            options={'verbose_name': 'Ichimlik', 'verbose_name_plural': 'Ichimliklar'},
        ),
        migrations.AlterModelOptions(
            name='buyurtmataom',
            options={'verbose_name': 'Taom', 'verbose_name_plural': 'Taomlar'},
        ),
    ]
