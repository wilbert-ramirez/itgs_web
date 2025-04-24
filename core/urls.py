from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('nosotros/', views.about, name='about'),
    path('servicios/', views.services, name='services'),
    path('contacto/', views.contact, name='contact'),
    path('experiencias/', views.experiencias, name='experiencias'),
    path('webhook/n8n/', views.webhook_n8n, name='webhook_n8n'),
]
