from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from instagramapp.models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

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

@login_required
def pag_inicio_instagram(request):
    return render( request, 'pag_inicio_instagram.html')

def perfil(request):
    return render( request, 'inicio_instagram.html')

@login_required
def uploadphoto(request):
    curr_user = request.user
    context = {'curr_user' : curr_user}
    return render(request, 'instagram/uploadphoto.html', context)    

@login_required
def uploadfile(request):
    curr_user = request.user
    Post_user = Post.objects.filter(creador=curr_user.id).count();
    mediaFile = request.FILES[ 'photo' ];
    newNameFile = curr_user.username + "-" + str(curr_user.id) + "-" + str(Post_user);
    fs = FileSystemstorage()
    filename = fs.save(newNameFile, mediaFile)
    uploaded_file_url = fs.url(filename)
    photo = uploaded_file_url;
    description = request.Post[ 'description' ];
    newPost = Post( foto = photo, descripcion = description, creador = curr_user );
    newPost.save();
    media_user = Post.objects.filter( creador =curr_user.id );
    context = { 'curr_user' : curr_user, 'media_user' : media_user }
    return render(request, 'intagram/profile.html', context )
