from django.urls import path
from .views import index
from .views import contacto

urlpatterns = [
    path('',index,name="index"),
    path('contacto/',contacto,name="contacto")
]