#serializers.py

from rest_framework import serializers
from V7_products.models import Product

class ProductSerializer(serializers.serializer):
	id = serializers.integerField(read_only=True)
	name = serializers.CharField()
	description = serializers.TextField()
	photo = serializers.ImageField()
	price = serializers.FloatField()
	Shipping_cost = serializers.FloatField()
	quantity = serializers.PositiveSmallIntegerField()

