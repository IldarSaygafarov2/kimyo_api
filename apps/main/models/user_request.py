from django.db import models
from apps.common.models import BaseTimedModel


class UserRequest(BaseTimedModel):
    name = models.CharField(verbose_name="Имя", max_length=150)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=14)
    company = models.CharField(verbose_name="Компания", max_length=150)
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self) -> str:
        return f"{self.name}: {self.phone_number}"

    class Meta:
        verbose_name = "Заявка пользователя"
        verbose_name_plural = "Заявки пользователей"
