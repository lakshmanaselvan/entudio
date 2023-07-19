from django.db import models

class Product(models.Model):
    product_name = models.CharField('Product Name',max_length=120)
    quantity = models.IntegerField('Quantity')
    rupees = models.IntegerField('Rupees')
    
    @property 
    def total(self):
        return self.quantity * self.rupees
    
    def __str__(self):
        return self.product_name
    
    