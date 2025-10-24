# Plataforma-de-Gestion-de-Eventos-M6_AE5_ABPRO

## 🗓️ Plataforma de Gestión de Eventos

Módulo 6
Bootcamp Desarrollo Full Stack Python

## 📌 Descripción

Aplicación web desarrollada en Django para gestionar eventos y participantes.
Permite registrar, editar y visualizar eventos según el rol del usuario, implementando autenticación, autorización y control de permisos.
El sistema garantiza una gestión segura y organizada de las acciones de cada usuario.

## ⚙️ Funcionalidades Principales

Autenticación completa: registro, inicio y cierre de sesión con UserCreationForm y AuthenticationForm.

Gestión de roles:

Administrador: acceso total (crear, editar, eliminar eventos).

Organizador: puede crear y editar eventos propios.

Asistente: puede ver los eventos en los que participa.

Control de permisos con Mixins: uso de LoginRequiredMixin, PermissionRequiredMixin y UserPassesTestMixin para proteger vistas.

Mensajes dinámicos: sistema django.contrib.messages para notificar acciones y errores.

Plantillas modulares: herencia (base.html y base_formulario.html) con Bootstrap 5.

Seguridad: configuración de sesiones seguras, CSRF y HTTPS.

## Decisiones de Diseño

Se utilizó el modelo de autenticación integrado de Django para aprovechar su seguridad y estructura de permisos.

Los roles se manejan mediante grupos creados desde el panel admin, lo que permite modificar permisos sin alterar el código.

Los Mixins personalizados (CustomPermissionMixin, AdminOrOrganizerRequiredMixin) centralizan la lógica de autorización, evitando repetir código en cada vista.

La relación ManyToMany entre Eventos y User permite que varios usuarios estén asociados a distintos eventos sin duplicar registros.

## 🧩 Tecnologías

Backend: Django 5

Base de datos: SQLite3

Frontend: HTML5, CSS3, Bootstrap 5.

Gestión de permisos: Django Auth + Mixins

## 🚀 Ejecución

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Luego abre http://127.0.0.1:8000/


## 👩‍💻 Autor

Sofía Lagos
Proyecto M6_AE5_ABPRO-Ejercicio grupal 
