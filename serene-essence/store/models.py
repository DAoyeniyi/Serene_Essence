from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("skincare", "Skincare"),
        ("bodycare", "Body Care"),
        ("makeup", "Makeup"),
        ("haircare", "Hair Care"),
        ("fragrance", "Fragrance"),
    ]

    name = models.CharField(max_length=200)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name