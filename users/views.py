#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from users.forms import LoginForm, UserEditForm, UserInscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import exceptions
from django.contrib.auth.models import User
from users.models import Client
from intra.pattern_decorators import loginGadz_required

def index(request):
    generalLogin(request)
    return render(request, "users/index.html")

def inscription(request):
    if request.method == 'POST':
        form = UserInscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(user.password)
            user.is_active = False
            user.save()
            messages.success(request, u"<strong>Création du compte réussie !</strong>")
            return redirect("users.views.index")
        else:
            messages.error(request, u"<strong>Erreur lors de la création du compte.</strong>")
    else:
        form = UserInscriptionForm()
    return render(request, "users/inscription.html", {'form' : form})

def loginForm(request):
	if request.user.is_authenticated():
		return redirect(index)
	form = generalLogin(request)
	if form == None:
		return redirect(index)
	return render(request, "users/login.html")

def generalLogin(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['user']
			password = form.cleaned_data['password']
			user = authenticate(username = user, password = password)
			if user and user.is_active:
				login(request, user)
				messages.success(request, u"<strong>Connection réussie.</strong>")
				return None
			elif user and not user.is_active:
				messages.error(request, u"<strong>Votre compte est désactivé ou en attente de validation, veuillez contacter un VP rézal.</strong>")
				return redirect("users.views.index")
			else:
				logout(request)
				messages.error(request, u"<strong>Erreur lors de la connection</strong><p>Mauvais nom d'utilisateur ou mauvais mot de passe.</p>")
				return redirect("users.views.loginForm")
		else:
			messages.error(request, u"<strong>Le formulaire n'est pas bien rempli</strong><p>Veuillez remplir les champs comme demandé.</p>")
			return redirect("users.views.loginForm")
	else:
		form = LoginForm()
	return form

@login_required
def logoutForm(request):
	logout(request)
	messages.success(request, u"<strong>Déconnection réussie.</strong>")
	return redirect("users.views.index", permanent = True)

@loginGadz_required
def getLinks(request):
	values = ['abc', 'bcd', 'cde']
	if request.GET.get('q'):
		l = request.GET['q']
	values = [elem for elem in values if l in elem]
	link = ""
	for elem in values:
		link += "<a class = 'item'>" + elem + "</a>"
	return HttpResponse(link)

@login_required
def settings(request):
	try:
		gadz = Client.objects.get(username = request.user.username)
		f = UserEditForm
		i = gadz
	except (AttributeError, exceptions.ObjectDoesNotExist):
		f = UserEditForm
		i = request.user
	if request.method == 'POST':
		form = f(request.POST, instance = i)
		if form.is_valid():
			form.save()
			messages.success(request, u"<strong>Enregistrement réussi.</strong>")
			return redirect("users.views.settings")
		else:
			messages.error(request, form.cleaned_data)
			messages.error(request, u"<strong>Erreur lors de l'enregistrement.</strong>")
			return redirect("users.views.settings")
	else:
		form = f(instance = i)
	return render(request, 'users/settings.html', {'form' : form})
