from django.urls import path
from modules.maaji.views import formularioContacto, contactar, hello_world


urlpatterns = [
    path('formularioContacto/', formularioContacto),
    path('formularioContacto/contactar/', contactar),
    path('helloworld/', hello_world)
]