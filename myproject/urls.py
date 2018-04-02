from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    url(r'^$', views.pagina_inicial, name = 'pagina_inicial'),
    url(r'^web/(\d+)$', views.pagina, name = 'recursos'),
    url(r'^admin/', include(admin.site.urls)),
)
