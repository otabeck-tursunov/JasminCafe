from django.db import models


class Joy(models.Model):
    raqam = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Joy'
        verbose_name_plural = 'Joylar'

    def __str__(self):
        return f"{self.raqam} - joy"
