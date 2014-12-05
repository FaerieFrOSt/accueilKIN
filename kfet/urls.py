from django.conf.urls import patterns, include, url

urlpatterns = patterns('kfet.views',
		url(r'^$', "index", name = 'index_kfet'),
		url(r'^products/$', "products", name = 'products'),
		url(r'^statistics/$', "statistics", name = 'statistics'),
		url(r'^getPg/', "getPg", name = 'getPg'),
		url(r'^getPgs/', "getPgs", name = "getPgs"),
)
