from django.db import models
from decimal import Decimal

# models for shop
class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True, verbose_name = 'Shop Id')
    shop_name = models.CharField(max_length=200, verbose_name = 'Shop Name')
    shop_owner = models.CharField(max_length=200, verbose_name = 'Shop owner')
    shop_address = models.CharField(max_length=200, verbose_name = 'Shop Address')
	
    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shop'
        ordering = ["shop_id"]
    def __str__(self):
        return str(self.shop_name)


# models for stocks 

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, verbose_name = 'Category Id')
    category_name = models.CharField(max_length=200, verbose_name = 'Category Name')
    category_description = models.CharField(max_length=200, verbose_name = 'Category Description')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ["category_id"]

    def __str__(self):
         return str(self.category_name)

class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True, verbose_name = 'Brand Id')
    brand_name = models.CharField(max_length=200, verbose_name = 'Brand Name')
    brand_description = models.CharField(max_length=200, verbose_name = 'Brand Description')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_p_cost = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_q_cost = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_n_cost = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_d_cost = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_l_cost = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_xg_cost = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_y_cost = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_p_sale = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_q_sale = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_n_sale = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_d_sale = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_l_sale = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_xg_sale = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    brand_y_sale = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    
	
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'
        ordering = ["brand_id"]

    def __str__(self):
         return str(self.brand_name)

class Invoice(models.Model):
    invoice_transaction_id = models.IntegerField(primary_key=True, verbose_name = 'Invoice Id')
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    invoice_brand_size = models.CharField(max_length=5, verbose_name = 'Brand Size')
    invoice_brand_qty = models.IntegerField(verbose_name = 'Brand Quantity')
    invoice_rate_per_case = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))
    invoice_no_of_bottles = models.IntegerField(verbose_name = 'Number of Bottles')
    invoice_total = models.DecimalField(max_digits=22, decimal_places=2,default=Decimal(0.00))    
    class Meta:
        verbose_name = 'invoice'
        verbose_name_plural = 'invoice'
        ordering = ["invoice_transaction_id"]

    def __str__(self):
         return str(self.invoice_transaction_id)

class Quantity(models.Model):
    quantity_name = models.CharField(primary_key=True,max_length=4, verbose_name = 'Quantity Name')
    quantity_bottles = models.IntegerField(verbose_name = 'Quantity bottles')

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'
        ordering = ["quantity_name"]

    def __str__(self):
         return str(self.quantity_name)