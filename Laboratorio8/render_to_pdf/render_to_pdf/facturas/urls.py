from django.urls import path
from .views import pdf_view
from .views import advanced_pdf_view
from .views import home_view
urlpatterns = [
    path('factura/', pdf_view, name='ver_factura_pdf'),
    path('factura-avanzada/', advanced_pdf_view, name='ver_factura_pdf_avanzada'),
    path("", home_view, name="home"),
]