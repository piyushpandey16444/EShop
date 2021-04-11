from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='uploads/products/')
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
