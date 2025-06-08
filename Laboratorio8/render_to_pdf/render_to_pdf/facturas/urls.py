from django.urls import path
from .views import pdf_view
urlpatterns = [
    path('factura/', pdf_view, name='ver_factura_pdf'),
]