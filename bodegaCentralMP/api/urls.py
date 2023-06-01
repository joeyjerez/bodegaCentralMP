from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('productos/', producto_list),
    path('productos/<int:codigo>', producto_detail),
]
