from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Eventos

class AdminOrOrganizerRequiredMixin(UserPassesTestMixin):
    """Mixin que permite acceso solo a administradores u organizadores"""
    permission_denied_redirect = 'inicio'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "Debes iniciar sesión para acceder a esta página.")
            return redirect('login')
        if not request.user.groups.filter(name__in=['Administrador', 'Organizador']).exists():
            messages.error(request, "No tienes permisos suficientes para acceder a esta página.")
            return redirect(self.permission_denied_redirect)
        return super().dispatch(request, *args, **kwargs)


class CustomPermissionMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """Mixin para manejar redirección en caso de permiso denegado"""
    permission_denied_redirect = 'inicio'

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.info(self.request, "Debes iniciar sesión para acceder a esta página.")
            return redirect('login')

        messages.error(self.request, "No tienes permisos suficientes para acceder a esta página.")
        return redirect(self.permission_denied_redirect)

class EventosRegistradosMixin(LoginRequiredMixin):
    model = Eventos
    template_name = 'lista_eventos'