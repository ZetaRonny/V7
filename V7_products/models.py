from django.db import models

# Create your models here.
class Manufacturer(models.Model):
	name = models.CharField(max_length=120)
	location = models.CharField(max_length=120)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,related_name="products")

	title = models.CharField(max_length=200, unique=True, default="n/a")
	slug = models.SlugField(max_length=200, unique=True, default="n/a")
	description = models.TextField(blank=True,null=True)
	image = models.ImageField(blank=True,null=True)
	price = models.FloatField()
	Shipping_cost = models.FloatField()
	quantity = models.PositiveSmallIntegerField()

	def __str__(self):
		return self.title
		
