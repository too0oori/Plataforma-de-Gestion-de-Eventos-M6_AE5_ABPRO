from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='root'),
    path('index/', views.index, name='inicio'),
    path('registro_evento/', views.registro_evento, name='registro_evento'),
    path('registro_usuario/', views.registro_user, name='registro_usuario'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
