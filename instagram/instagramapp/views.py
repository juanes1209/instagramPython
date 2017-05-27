from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from instagramapp.models import *

# Create your views here.
def registro(request):
    return render( request, 'registro_del_instagram.html')

def crear_usuario ( request ):
    _email=request.POST['email']
    _username = request.POST['username']
    _name=request.POST['name']
    _password=request.POST['password']
    print (_email)
    print (_username)
    print (_password)
    print (_name)
    user=User .objects.create_user(username= _username, email=_email,
                                    password=_password, first_name=_name )
    myUser= MiUsuario( usuario=user )
    myUser.save
    print (user)
    print (user.password)
    return redirect('tienes_cuenta')


def tienes_cuenta(request):
    return render( request, 'tienes_cuenta.html')
