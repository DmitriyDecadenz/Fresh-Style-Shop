from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=150, unique=True)

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="URL",
    )
    description = models.TextField()
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    amount = models.PositiveIntegerField(default=0, null=True)
    Price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    category = models.ForeignKey("Category", models.CASCADE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} ({self.pk})"
