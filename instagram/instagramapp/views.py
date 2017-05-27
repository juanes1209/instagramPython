from django.shortcuts import render

# Create your views here.
def registro(request):
    return render( request, 'registro.html')

def crear_usuario ( request ):
    email=request
    username = request.POST['Nombre de Usuario']
     name=(request.POST['Nombre Completo']
    return render( request, 'pag_inicio_instagram.html')
    print(email)
    print(username)
    print(password)
    print(name)

def tienes_cuenta(request):
    return render( request, 'tienes_cuenta.html')
