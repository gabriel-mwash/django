from django.db import models

# Create your models here.


class Product(models.Model):

    # basic datatypes
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.IntegerField(default=0)
    is_active= models.BooleanField(default=True)

    # dates
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # choices
    CATEGORY_CHOICES = [
            ("Elec", "Electronics"),
            ("HOME", "Home & Garden"),
            ("TOYS", "Toys"),
    ]

    category = models.CharField(
            max_length=4, choices=CATEGORY_CHOICES, default="ELEC"
            )

    # danda method
    def __str__(self):
        return f"{self.name} (${self.price})"

    class Meta:
        ordering = ["-price"]
        verbose_name_plural = "Products"
