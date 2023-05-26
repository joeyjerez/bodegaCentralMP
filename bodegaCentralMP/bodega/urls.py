"""
URL configuration for bodegaCentralMP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path('', root),
    path('bodega', index, name="index"),
    path('bodega/login', login, name="login"),
    path('bodega/productos', productos_list, name="productos_list"),
    path('bodega/productos/new', productos_new, name="productos_new"),
    path('bodega/productos/<int:codigo>/edit', productos_edit, name="productos_edit"),
    path('bodega/productos/<int:codigo>/delete', productos_delete, name="productos_delete"),
    path('bodega/usuarios', usuarios_list, name="usuarios_list"),
    path('bodega/usuarios/new', usuarios_new, name="usuarios_new"),
    path('bodega/usuarios/<str:rut>/edit', usuarios_edit, name="usuarios_edit"),
    path('bodega/usuarios/<str:rut>/delete', usuarios_delete, name="usuarios_delete"),
]
