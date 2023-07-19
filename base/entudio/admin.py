from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product

#admin.site.register(Product)

@admin.register(Product)
class ProductEvent( ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('product_name','quantity','rupees','total')
    ordering =('id',)
    search_fields = ('product_name','quantity')
