import datetime
from django.http import Http404
from django.shortcuts import render
from render_to_pdf.renderers import render_to_pdf 
# Create your views here.
def pdf_view(request, *args, **kwargs):
    data = {
        'date': datetime.date.today(),
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'invoice_number': 1233434,
        'pdf_title': 'Factura PDF'
    }
    return render_to_pdf('pdftemplates/pdfsinvoice.html', data)