from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import EventoForm, UserRegisterForm
from .models import Eventos
from .mixins import AdminOrOrganizerRequiredMixin, CustomPermissionMixin, EventosRegistradosMixin


# Create your views here.
def index(request):
    return render(request, 'index.html')

class RegistroEventoView(CustomPermissionMixin, CreateView):
    model = Eventos
    form_class = EventoForm
    template_name = 'registro_evento.html'
    success_url = reverse_lazy('lista_eventos')
    
    login_url = 'login'
    permission_required = 'eventos.add_eventos'
    raise_exception = True

    def form_valid(self, form):
        # Guardar el evento primero
        self.object = form.save()
        # Agregar automáticamente al usuario que creó el evento
        self.object.usuarios_registrados.add(self.request.user)
        messages.success(self.request, f"Evento '{self.object.nombre}' creado exitosamente.")
        return redirect(self.get_success_url())


class SignupView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "registration/signup.html", {"form": form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

                        # Se agraga cada usuario creado de inmeadiato a "Asistentes"
            asistentes_group, created = Group.objects.get_or_create(name='Asistentes')
            user.groups.add(asistentes_group)

            login(request, user)
            messages.success(request, f"¡Bienvenido {user.username}!")
            return redirect("inicio")
        return render(request, "registration/signup.html", {"form": form})
    
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "registration/login.html", {"form": form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_eventos')
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user_groups = self.request.user.groups.values_list('name', flat=True)
        
        # EDITAR: Organizadores Y Administradores (y superusuario)
        puede_editar = (
            'Organizadores' in user_groups or 
            'Administrador' in user_groups or 
            self.request.user.is_superuser
        )
        
        # ELIMINAR: Solo Administradores (y superusuario)
        puede_eliminar = (
            'Administrador' in user_groups or 
            self.request.user.is_superuser
        )

        puede_ver = (
            'Asistentes' in user_groups or
            'Organizadores' in user_groups or 
            'Administrador' in user_groups or 
            self.request.user.is_superuser
        )
        
        return context

class EditarEventoView(CustomPermissionMixin, UserPassesTestMixin, UpdateView):
    model = Eventos
    form_class = EventoForm
    template_name = 'editar_evento.html'
    success_url = reverse_lazy('lista_eventos')
    permission_required = 'eventos.change_eventos'

    def test_func(self):
        # Solo administradores y organizadores pueden editar
        return (
            self.request.user.groups.filter(name__in=['Administrador', 'Organizadores']).exists()
            or self.request.user.is_superuser
        )

    def form_valid(self, form):
        messages.success(self.request, f"Evento '{self.object.nombre}' actualizado exitosamente.")
        return super().form_valid(form)

class EliminarEventoView(CustomPermissionMixin, UserPassesTestMixin, DeleteView):
    model = Eventos
    template_name = 'eliminar_evento.html'
    success_url = reverse_lazy('lista_eventos')
    permission_required = 'eventos.delete_eventos'

    def test_func(self):
        # Solo administradores pueden eliminar
        return (
            self.request.user.groups.filter(name='Administrador').exists()
            or self.request.user.is_superuser
        )