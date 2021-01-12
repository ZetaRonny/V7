from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save , m2m_changed


from V7_products.models import Product

User = settings.AUTH_USER_MODEL

# Create your models here.

class CartManager(models.Manager):
	def get_or_create():
		return obj, True

	def new_or_get(self, request):
		cart_id = request.session.get('cart_id',None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_obj = False
			cart_obj = qs.first()
			if request.user.is_authenticated and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = self.new(user=request.user)
			new_obj = True
			request.session['cart_id'] = cart_obj.id
		return cart_obj

	def new(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated:
				user_obj = user
		return self.model.objects.create(user=user_obj)

class Cart(models.Model):
	user      = models.ForeignKey(User, null=True, blank=True, default= None, on_delete=models.CASCADE) 
	products  = models.ManyToManyField(Product, blank=True)
	subtotal  = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	total     = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
	updated   = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)


def m2m_changed_cart_reciever(sender, instance, action, *args, **kwags):
	if action == 'post_add' or action == 'post_remove' or action =='post_clear':
		products = instance.products.all()
		total = 0
		for product in products:
			total += product.price
		instance.total = total
		instance.save()


m2m_changed.connect(m2m_changed_cart_reciever, sender=Cart.products.through)

def pre_save_changed_cart_reciever(sender, instance, *args, **kwags):
	instance.total = instance.subtotal

pre_save.connect(pre_save_changed_cart_reciever, sender=Cart)