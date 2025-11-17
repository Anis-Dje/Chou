from django.db import models

# Create your models here.
class Order(models.Model):
    quantity = models.PositiveIntegerField()
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.full_name}"
