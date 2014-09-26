from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.models import User
from django.core import exceptions
from users.models import Client

def	loginGadz_required(function):
    @login_required
    def	modified_function(request, *args, **kwargs):
        try:
	    gadz = Client.objects.get(username = request.user.username)
            if not gadz.is_gadz:
                return redirect("users.views.index")
        except (AttributeError, exceptions.ObjectDoesNotExist):
            return redirect("users.views.index")
        return function(request, *args, **kwargs)
    return modified_function
