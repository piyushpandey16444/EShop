from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        "store.Category", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)
    description = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='uploads/products/')
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()
