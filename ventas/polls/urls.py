from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:nombre>/<str:email>/<str:telefono>/<str:direccion>/<str:forma_pago>/<str:precio>/', views.detail, name='detail'),
]