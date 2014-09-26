#-*- encoding: utf-8 -*-
from django.db import models
from django.db.models import F
from django.core.exceptions import ValidationError

# Entité (Kfet, Cvis, etc...)
class Entity(models.Model):
	name = models.CharField(max_length = 32)

	def __unicode__(self):
		return self.name

# Catégorie de produits (binouse, remise d'argent, etc...)
class Category(models.Model):
	name = models.CharField(max_length = 32)
	color = models.CharField(max_length = 16)
	entity = models.ForeignKey('Entity')

	def __unicode__(self):
		return self.name

# Produit (kro, remise chèque, etc...)
class Product(models.Model):
	name = models.CharField(max_length = 255)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	reference = models.CharField(max_length = 8)
	category = models.ForeignKey('Category')

	def __unicode__(self):
		return self.name

# achat d'un produit par un pg, vendu par un autre pg
class Order(models.Model):
	product = models.ForeignKey('Product')
	gadz = models.ForeignKey('users.Client', related_name = 'user_gadz')
	vendor = models.ForeignKey('users.Client', related_name = 'user_vendor')
	total_price = models.DecimalField(max_digits = 5, decimal_places = 2, blank = True)
	number_of_products = models.SmallIntegerField(blank = True)
	date = models.DateTimeField(auto_now_add = True, auto_now = False)
        message = models.TextField(blank = True)

	def clean(self):
		if self.total_price == None and self.number_of_products:
			self.total_price = self.product.price * self.number_of_products
		elif self.total_price and self.number_of_products == None:
			self.number_of_products = self.total_price / self.product.price
			if self.number_of_products * self.product.price != self.total_price:
				raise ValidationError(u"Not the right total price")
		elif self.total_price == None and self.number_of_products == None:
			self.total_price = self.product.price
			self.number_of_products = 1
		if self.gadz.credit - self.total_price < 0:
			raise ValidationError(u"Not enought money on {0} for {1}".format(self.gadz.user.username, self.product.name))

	def save(self, *args, **kwargs):
		self.gadz.credit = F('credit') - self.total_price
		self.gadz.save()
		super(Order, self).save(*args, **kwargs)

	def __unicode__(self):
		return u"{0} selled to {1} by {2}".format(self.product.name, self.gadz.user.username, self.vendor.user.username)
