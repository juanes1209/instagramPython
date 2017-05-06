from django.conf.urls import url

from . import views

urlpatterns = [
   url (r'^$', views.registro, name = 'registro'),
   url (r'^tienes_cuenta/$',views.tienes_cuenta, name='tienes_cuenta' )
]
