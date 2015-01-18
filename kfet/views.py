# coding: utf-8
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.contrib import messages

from django.core.urlresolvers import reverse

from kfet.models import Order, Product
from users.models import Client
from intra.pattern_decorators import loginGadz_required

import json

@loginGadz_required
def index(request):
	orders = Order.objects.order_by('date')[:10]
	return render(request, 'kfet/index.html', {'orders' : orders})

@loginGadz_required
def products(request):
	products = Product.objects.order_by('category__entity__name')
	orders = Order.objects.order_by('date')[:10]
	return render(request, 'kfet/products.html', {'products' : products, 'orders' : orders})

@loginGadz_required
def statistics(request):
	orders = Order.objects.order_by('date')[:10]
	return render(request, 'kfet/statistics.html', {'products' : products, 'orders' : orders})

@loginGadz_required
def getPgs(request):
	data = []
	try:
		pg = request.GET.get('pg', '')
		data = Client.objects.filter(username__icontains = pg)
	except (KeyError, exceptions.ObjectDoesNotExist, ValueError):
		pass
	tmp = {}
	tmp["results"] = []
	for i in data:
		tmp["results"].append({"title" : i.username, "url" : "{0}?pg={1}".format(reverse("getPg"), i.id)})
	return HttpResponse(json.dumps(tmp), content_type = "text/javascript")

@loginGadz_required
def getPg(request):
	pg = ''
	try:
		pg = request.GET.get('pg', '')
		if pg != '':
			pg = Client.objects.get(id = int(pg))
		else:
			messages.warning(request, u"<strong>L'utilisateur demandé n'a pas été trouvé.</strong>")
			return redirect(index, permanent = True)
	except (KeyError, exceptions.ObjectDoesNotExist, ValueError):
		messages.warning(request, u"<strong>L'utilisateur demandé n'a pas été trouvé</strong>")
		return redirect(index, permanent = True)
	orders = Order.objects.order_by('date')[:10]
	return render(request, 'kfet/print_pg.html', {'orders' : orders, 'pg' : pg})
