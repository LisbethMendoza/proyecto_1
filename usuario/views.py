from django.shortcuts import render, redirect
from .models import Usuario  

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(username=username)
            if usuario.password == password:
                request.session['user_id'] = usuario.id
                return redirect('index')  
            else:
                error = "Usuario o contraseña incorrectos."
        except Usuario.DoesNotExist:
            error = "Usuario o contraseña incorrectos."

    return render(request, 'usuario/login.html', {'error': error})

def index_view(request):
    if 'user_id' not in request.session:
        return redirect('login')  
    return render(request, 'usuario/hotel/index.html')
