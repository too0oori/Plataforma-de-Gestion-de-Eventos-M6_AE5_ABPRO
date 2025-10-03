from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro_evento(request):
    if request.method == 'POST':
        # Aquí iría la lógica para procesar el formulario de registro
        pass
    return render(request, 'registro_evento.html')

def registro_user(request):
    if request.method == 'POST':
        # Aquí iría la lógica para procesar el formulario de registro de usuario
        pass
    return render(request, 'registro_user.html')

def login_view(request):
    if request.method == 'POST':
        # Aquí iría la lógica para procesar el formulario de login
        pass
    return render(request, 'templates/login.html')

def logout_view(request):
    # Aquí iría la lógica para cerrar sesión
    return render(request, 'templates/logout.html')

def signup_view(request):
    if request.method == 'POST':
        # Aquí iría la lógica para procesar el formulario de signup
        pass
    return render(request, 'signup.html')

