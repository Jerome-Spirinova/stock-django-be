from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'  # Specify the exact table name

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stocks = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'  # Specify the exact table name