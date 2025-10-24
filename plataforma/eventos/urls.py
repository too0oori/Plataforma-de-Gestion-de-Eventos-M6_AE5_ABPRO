from django.urls import path
from .views import (index, RegistroEventoView, SignupView, ListaEventosRegistradosView,
                    EditarEventoView, EliminarEventoView)
from .views import custom_logout
from . import views

urlpatterns = [
    path('', index, name='root'),
    path('index/', index, name='inicio'),
    path('registro_evento/', RegistroEventoView.as_view(), name='registro_evento'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', views.custom_logout, name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('lista_eventos/', views.ListaEventosRegistradosView.as_view(), name='lista_eventos'),
    path('editar_evento/<int:pk>/', EditarEventoView.as_view(), name='editar_evento'),
    path('eliminar_evento/<int:pk>/', EliminarEventoView.as_view(), name='eliminar_evento'),
]
