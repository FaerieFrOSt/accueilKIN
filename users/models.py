#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core import exceptions

import hashlib
import base64
import os

class   radcheck(models.Model):
    username = models.CharField(max_length = 64)
    attribute = models.CharField(max_length = 64)
    op = models.CharField(max_length = 2, default = '==')
    value = models.CharField(max_length = 253)
    
    class Meta:
        db_table = 'radcheck'

class Client(User):
	bucque = models.CharField(blank = True, max_length = 255)
	avatar = models.ImageField(null = True, blank = True, upload_to = "/static/avatar/")
	signature = models.TextField(blank = True)
	credit = models.DecimalField(default = 0.0, max_digits = 5, decimal_places = 2)
	famss = models.CharField(blank = True, max_length = 255, verbose_name = u"Fam'ss")
	promss = models.IntegerField(null = True, blank = True, verbose_name = u"prom'ss")
	kgibss = models.CharField(max_length = 4, verbose_name = u"Chambre")
	phone = models.CharField(max_length = 10, verbose_name = u"Téléphone")
	date_negatss = models.DateTimeField(blank = True, null = True)
	has_rezal = models.BooleanField(default = False)
	is_gadz = models.BooleanField(default = False)
	is_debucquable = models.BooleanField(default = False)
	radcheck_password = models.CharField(max_length = 253)
        
	def set_password(self, password):
		super(Client, self).set_password(password)
		salt = os.urandom(4)
		h = hashlib.sha1(password)
		h.update(salt)
		self.radcheck_password = base64.b64encode(h.digest() + salt)
            
	def save(self, *args, **kwargs):
		super(Client, self).save(*args, **kwargs)
		if self.is_active:
			tmp, created = radcheck.objects.get_or_create(username = self.username, attribute  = 'SSHA-Password', op = ':=', value = self.radcheck_password)
		else:
			try:
				tmp = radcheck.objects.get(username = self.username, value = self.radcheck_password)
				tmp.delete()
			except (exceptions.ObjectDoesNotExist, exceptions.MultipleObjectsReturned):
				return
					
	def __unicode__(self):
		return u"%s %s" %(self.first_name, self.last_name)
