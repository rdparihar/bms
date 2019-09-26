from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


# models for stocks 

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, verbose_name = 'Category Id')
    category_name = models.CharField(max_length=200, verbose_name = 'Category Name')
    category_description = models.CharField(max_length=200, verbose_name = 'Category Description')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ["category_id"]
        permissions = (("can_see_category", "Can see category"),) 

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
        verbose_name_plural = 'Brands'
        ordering = ["brand_id"]

    def __str__(self):
         return str(self.brand_name)


class Quantity(models.Model):
    quantity_name = models.CharField(primary_key=True,max_length=4, verbose_name = 'Quantity Name')
    quantity_bottles = models.IntegerField(verbose_name = 'Quantity bottles')

    class Meta:
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'
        ordering = ["quantity_name"]

    def __str__(self):
         return str(self.quantity_name)

class BmsUser(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.IntegerField(primary_key=True, verbose_name = 'User Id')
    user_first_name = models.CharField(max_length=50, verbose_name = 'First Name')
    user_last_name = models.CharField(max_length=50, verbose_name = 'Last Name')
    user_role = models.IntegerField(verbose_name = 'User Role')

    class Meta:
        verbose_name = 'Bms User'
        verbose_name_plural = 'Bms User'
        ordering = ["-user_id"]

    def __str__(self):
         return str(self.username)

# models for shop
class Shop(models.Model):
    shop_id = models.IntegerField(primary_key=True, verbose_name = 'Shop Id')
    shop_name = models.CharField(max_length=200, verbose_name = 'Shop Name')
    shop_owner = models.CharField(max_length=200, verbose_name = 'Shop owner')
    shop_address = models.CharField(max_length=200, verbose_name = 'Shop Address')
    shop_admin = models.ForeignKey(BmsUser, on_delete=models.CASCADE)
	
    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shop'
        ordering = ["shop_id"]
    def __str__(self):
        return str(self.shop_name)

class Shift(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock_shift_date = models.DateField(verbose_name = 'Stock Shift Date')
    stock_shift_from = models.IntegerField(verbose_name = 'Stock Shift From Shop')
    stock_shift_to = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name = 'Stock Shift To Shop')
    stock_shift_p = models.IntegerField(verbose_name = 'Stock Shift P')
    stock_shift_q = models.IntegerField(verbose_name = 'Stock Shift Q')
    stock_shift_n = models.IntegerField(verbose_name = 'Stock Shift N')
    stock_shift_d = models.IntegerField(verbose_name = 'Stock Shift D')
    stock_shift_l = models.IntegerField(verbose_name = 'Stock Shift L')
    stock_shift_xg = models.IntegerField(verbose_name = 'Stock Shift XG')
    stock_shift_y = models.IntegerField(verbose_name = 'Stock Shift Y')

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'
        ordering = ["stock_shift_date"]

    def __str__(self):
         return str(self.stock_shift_date)

class Invoice(models.Model):
    invoice_transaction_id = models.IntegerField(primary_key=True, verbose_name = 'Invoice Id')
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
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