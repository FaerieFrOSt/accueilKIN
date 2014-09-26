from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
		url(r'^$', "index"),
		url(r'^index/$', "index", name = 'index_users'),
		url(r'^logout/$', "logoutForm", name = 'logout'),
		url(r'^login/$', "loginForm", name = 'login'),
		url(r'^getLinks/', "getLinks", name = 'links'),
		url(r'^settings/$', "settings", name = 'settings'),
		url(r'^inscription/$', "inscription", name = 'inscription'),
)
