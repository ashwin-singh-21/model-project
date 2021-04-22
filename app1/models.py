from django.db import models


# Create your models here.
class mymodel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    details = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = (
        ('clothes','clothes'),
        ('it', 'it'),
        ('electronics', 'electronics'),
        ('sports', 'sports')

    )
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField(max_length=200, choices=Category, default='it')
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='uploads/products_img')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class orders(models.Model):
    Status = (
        ('completed', 'completed'),
        ('pending', 'pending')
    )
    product_n = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    status = models.CharField(max_length=200, choices=Status)

    tag = models.ManyToManyField(Tag, null=True)
