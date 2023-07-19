from django.shortcuts import render
from .models import Product
from django.http import FileResponse, HttpResponseRedirect, HttpResponse
import io
from django.template.loader import get_template
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.views.generic import View
from .utils import html_to_pdf
from fpdf import FPDF

class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         
        # getting the template
        pdf = html_to_pdf('pdf.html')
        products = Product.objects.all()
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf',)
        return render()

def home(request):
    return render(request, "home.html", {})


def product_list(request):
    product_list = Product.objects.all().order_by('product_name')
    return render(request, "productlist.html", {'product_list':product_list})

def pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    products = Product.objects.all()
    lines=[
        "Endutio Product List:"
    ]
    for product in products:
        lines.append(" ")
        lines.append("ProductName:" + " " +product.product_name)
        lines.append("Quantity:" + " " +str(product.quantity))
        lines.append("Rupees:" + " " +str(product.rupees))
        lines.append("Total:" + " " +str(product.total))
        lines.append(" ")
        lines.append("==================================================")
        
        
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="stock.pdf")
    
    

