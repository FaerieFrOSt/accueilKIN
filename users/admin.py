from django.contrib import admin
from users.models import Client

class   AdminClient(admin.ModelAdmin):
	fieldsets = (
				(u"Utilisateur", {
						'classes' : ('collapse', 'open'),
						'fields' : ('username', 'first_name', 'last_name', 'phone', 'kgibss', 'email', 'is_active', 'has_rezal')
						}),)

admin.site.register(Client, AdminClient)
