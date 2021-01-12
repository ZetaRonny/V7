import random
import os
from django.urls import reverse
from django.db.models import Q
from django.db import models

# Create your models here.

STATUS = (
    (0,"Vaulted"),
    (1,"Available")
)

def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name , ext = os.path.splitext(filename)
    return name , ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)

class ProductManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) | 
                         Q(description__icontains=query)|
                         Q(slug__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

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
	price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	featured = models.BooleanField(default=False)
	Shipping_cost = models.FloatField()
	quantity = models.PositiveSmallIntegerField()

	objects = ProductManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('products:detail', kwargs={'slug': self.slug})

 


		
