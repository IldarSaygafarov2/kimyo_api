from django.db import models
from apps.common.models import BaseTimedModel


class Industry(BaseTimedModel):
    name = models.CharField(verbose_name="Название", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Отрасль"
        verbose_name_plural = "Отрасли"
