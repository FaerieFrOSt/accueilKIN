# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import exceptions
from django.contrib import messages

from kfet.models import Order, Product
from users.models import Client
from intra.pattern_decorators import loginGadz_required

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
def	print_pg(request):
	try:
		pg = request.GET['search_pg']
		pg = Client.objects.get(id = pg)
	except (KeyError, exceptions.ObjectDoesNotExist, ValueError):
		messages.warning(request, u"<strong>L'utilisateur demandé n'a pas été trouvé</strong>")
		return redirect(index, permanent = True)
	orders = Order.objects.order_by('date')[:10]
	return render(request, 'kfet/print_pg.html', {'orders' : orders, 'pg' : pg})
