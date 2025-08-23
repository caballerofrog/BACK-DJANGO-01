from django.urls import path
from . import views
urlpatterns=[
    path('', views.showInicio, name="inicio"),
    path('presentacion/', views.showPresentacion, name="presentacion"),
    path('catalogo/', views.showCatalogo, name="catalogo")
]