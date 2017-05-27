from django.conf.urls import url

from . import views

urlpatterns = [
   url (r'^$', views.registro, name = 'registro'),
   url (r'^crear_usuario/$',views.crear_usuario, name='crear_usuario' ),
   url (r'^tienes_cuenta/$',views.tienes_cuenta, name='tienes_cuenta' ),
]
