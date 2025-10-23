from urllib import request
from django.shortcuts import render
from .forms import EventoForm
from .forms import UserRegisterForm
from .models import Eventos
from .mixins import AdminOrOrganizerRequiredMixin, CustomPermissionMixin, EventosRegistradosMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LogoutView



# Create your views here.
def index(request):
    return render(request, 'index.html')

class RegistroEventoView(CustomPermissionMixin, CreateView):
    model = Eventos
    form_class = EventoForm
    template_name = 'registro_evento.html'
    success_url = reverse_lazy('lista_eventos.html')
    
    login_url = 'login'
    permission_required = 'eventos.add_eventos'
    raise_exception = True


class SignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"¡Bienvenido {user.username}!")
            return redirect("index")
    
class LoginView(View):
    def get(self, request):
        
        form = AuthenticationForm()
        return render(request, "registration/login.html", {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_eventos.html')
        return render(request, "registration/login.html", {"form": form})
    
def custom_logout(request):
    logout(request)
    messages.info(request, "Has cerrado sesión exitosamente.")
    return redirect("inicio")

class ListaEventosRegistradosView(EventosRegistradosMixin, ListView):
    model = Eventos
    template_name = 'lista_eventos.html'
    context_object_name = 'eventos'
    def get_queryset(self):
        # Solo muestra eventos del usuario autenticado
        return Eventos.objects.filter(usuarios_registrados=self.request.user)