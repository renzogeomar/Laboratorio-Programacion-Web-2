from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('destinos/', views.destinos, name='destinos'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('destinos/', views.listar_destinos, name='listar_destinos'),
    path('destinos/nuevo/', views.crear_destino, name='crear_destino'),
    path('destinos/editar/<int:id>/', views.modificar_destino, name='modificar_destino'),
    path('destinos/eliminar/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
]

