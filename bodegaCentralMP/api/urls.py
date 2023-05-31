o
    t@pd�  �                   @   sN   d Z ddlmZ ddlmZ edejdd�edejd	d�ed
ejdd�gZdS )a�  
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
�    )�path�   )�viewszlogin/�login)�namezindex/�indexzlogout/�logoutN)	�__doc__�django.urlsr   � r   Z
login_viewZ
index_viewZlogout_view�urlpatterns� r   r   �8C:\GitHub\bodegaCentralMP\bodegaCentralMP\bodega\urls.py�<module>   s    �