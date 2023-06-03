from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('', root),
    path('productos/', producto_list),
    path('productos/<int:codigo>', producto_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)