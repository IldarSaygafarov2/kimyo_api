import uuid

from django.db import models



class BaseTimedModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name="ID", editable=False)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        abstract = True
