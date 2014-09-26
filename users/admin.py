# -*- coding: utf8 -*-
from django.contrib import admin
from users.models import Client

class   AdminClient(admin.ModelAdmin):
	list_display = ('__str__', 'is_active', 'has_rezal', 'kgibss', 'phone', 'email')
	list_filter = ('is_active', 'has_rezal')
	search_fields = ('first_name', 'last_name', 'kgibss', 'phone', 'email')
	fieldsets = (
				(u"Utilisateur", {
						'classes' : ('gr-collapse grp-closed'),
						'fields' : ('username', 'first_name', 'last_name', 'phone', 'kgibss', 'email', 'is_active', 'has_rezal')
						}),)
	actions = ['set_rezal', 'remove_rezal', 'set_active', 'remove_active']

	def set_rezal(self, request, queryset):
		queryset.update(has_rezal = True)
	set_rezal.short_description = u"Activer le rézal pour les utilisateurs sélectionnés"

	def remove_rezal(self, request, queryset):
		queryset.update(has_rezal = False)
	remove_rezal.short_description = u"Désactiver le rézal pour les utilisateurs sélectionnés"

	def set_active(self, request, queryset):
		queryset.update(is_active = True)
	set_active.short_description = u"Activer les utilisateurs sélectionnés"

	def remove_active(self, request, queryset):
		queryset.update(is_active = False)
	remove_active.short_description = u"Désactiver les utilisateurs sélectionnés"

admin.site.register(Client, AdminClient)
