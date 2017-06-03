from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   url (r'^$', views.registro, name = 'registro'),
   url (r'^crear_usuario/$',views.crear_usuario, name='crear_usuario' ),
   url (r'^tienes_cuenta/$',views.tienes_cuenta, name='tienes_cuenta' ),
   url (r'^pag_inicio_instagram/$',views.pag_inicio_instagram, name='pag_inicio_instagram'),
   url (r'^login/$', auth_views.LoginView.as_view(template_name='tienes_cuenta.html',redirect_authenticated_user=True),name='login' ),
   url (r'^logout/$', auth_views.LogoutView.as_view(template_name='pag_inicio_instagram.html'),name= 'logout' ),
   url (r'^perfil/$',views.perfil, name='perfil' ),




]
