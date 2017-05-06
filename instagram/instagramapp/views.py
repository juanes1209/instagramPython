from django.shortcuts import render

# Create your views here.
def registro(request):
    return render( request, 'registro.html')

def tienes_cuenta(request):
    return render( request, 'tienes_cuenta.html')
