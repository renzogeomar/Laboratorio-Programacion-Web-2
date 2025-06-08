import datetime
from django.http import Http404
from django.shortcuts import render
from render_to_pdf.renderers import render_to_pdf 
import locale
locale.setlocale(locale.LC_ALL, "")

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

def advanced_pdf_view(request):
    invoice_number = "007cae"
    context = {
        "customer_name": "Ethan Hunt",
        "invoice_number": f"{invoice_number}",
        "amount": locale.currency(100_000, grouping=True),
        "date": "2021-07-04",
        "pdf_title": f"Invoice #{invoice_number}",
    }
    response = render_to_pdf("pdftemplates/pdfsinvoice.html", context)

    if response.status_code == 404:
        raise Http404("Invoice not found")

    filename = f"Invoice_{invoice_number}.pdf"

    # Por defecto se mostrará en el navegador
    content = f"inline; filename={filename}"

    # Si se pasa el parámetro ?download=1, se forzará la descarga
    if request.GET.get("download"):
        content = f"attachment; filename={filename}"

    response["Content-Disposition"] = content
    return response