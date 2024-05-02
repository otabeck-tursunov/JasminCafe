from django.db import models


class Taom(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    narx = models.IntegerField()

    class Meta:
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'

    def __str__(self):
        return self.nom


class Ichimlik(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    narx = models.IntegerField()

    class Meta:
        verbose_name = 'Ichimlik'
        verbose_name_plural = 'Ichimliklar'

    def __str__(self):
        return self.nom


