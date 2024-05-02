from django.db import models

from joyApp.models import Joy
from mainApp.models import Ichimlik, Taom
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction




class Buyurtma(models.Model):
    raqam = models.AutoField(primary_key=True)
    joy = models.ForeignKey(Joy, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    hisoblandi = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    def __str__(self):
        return f"{self.joy}. Buyurtma raqami: {self.raqam}"


class BuyurtmaIchimlik(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    ichimlik = models.ForeignKey(Ichimlik, on_delete=models.CASCADE)
    soni = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Ichimlik'
        verbose_name_plural = 'Ichimliklar'


class BuyurtmaTaom(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    taom = models.ForeignKey(Taom, on_delete=models.CASCADE)
    soni = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Taom'
        verbose_name_plural = 'Taomlar'


@receiver(post_save, sender=BuyurtmaTaom)
def update_buyurtma_hisoblandi(sender, instance, **kwargs):
    with transaction.atomic():
        buyurtma = instance.buyurtma
        soni = instance.soni
        narx = instance.taom.narx
        buyurtma.hisoblandi += soni * narx
        buyurtma.save()