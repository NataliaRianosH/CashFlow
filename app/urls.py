from django.urls import path, include
from django.contrib import admin
from . import views
from app import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'gastos', views.ConceptoGastosViewSet, 'gastos')

urlpatterns = [
  
 #   path('', views.concepto_gastos),
    path('', include(router.urls)),

  #  path('new/', views.crear_concepto_gastos, name="nuevo_concepto"),
  #  path('eliminar_concepto/<int:concepto_id>/', views.eliminar_concepto_gasto, name="eliminar_concepto"),
   # path('modificar_concepto/<int:concepto_id>/', views.modificar_concepto, name='modificar_concepto'),
  #  path('api/', include(router.urls))   
]
