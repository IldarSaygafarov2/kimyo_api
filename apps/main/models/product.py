from django.db import models

from apps.common.models import BaseTimedModel


class Product(BaseTimedModel):
    name = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(
        verbose_name="Короткая ссылка",
        help_text="Данное поле заполняется автоматически",
    )
    formula = models.CharField(max_length=50, verbose_name="Формула")
    description_1 = models.TextField(
        verbose_name="Первая часть описания",
        null=True,
        blank=True,
    )
    description_2 = models.TextField(
        verbose_name="Вторая часть описания",
        null=True,
        blank=True,
    )
    image = models.ImageField(verbose_name="Фото", upload_to="products/")
    category = models.ManyToManyField(
        "main.Category",
        related_name="products",
        verbose_name="Категория",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductApplication(BaseTimedModel):
    name = models.CharField(verbose_name="Название", max_length=150)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name="Товар",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Применение"
        verbose_name_plural = "Применение"
