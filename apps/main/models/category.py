from django.db import models
from apps.common.models import BaseTimedModel


class Category(BaseTimedModel):
    name = models.CharField(verbose_name="Название", max_length=150)
    slug = models.SlugField(
        verbose_name="Короткая ссылка",
        help_text="Данное поле заполняется автоматически",
    )
    image = models.ImageField(verbose_name="Фото", upload_to="categories/previews/")
    short_description = models.TextField(verbose_name="Краткое описание")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
