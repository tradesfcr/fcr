from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

#----------User Detail Table---------------

class UserDetail(models.Model):
    user_ref = models.ForeignKey(User,related_name='user_detail', on_delete=models.CASCADE,verbose_name="User Id")
    role_ref = models.ForeignKey('RoleMaster', on_delete=models.CASCADE)
    # profile_image = models.ImageField(upload_to='profile_images/')
    profile_image = models.CharField(max_length=255)
    address = models.TextField()
    contact_no = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    to_show = models.BooleanField(default=True)

    # class Meta:
    #     db_table = "tbl_user_detail"

    def __str__(self):
        return self.title

#-------------User Detail Table End-----------
        
#-------------All Master Table Start----------

class AllMaster(models.Model):
    master_type = models.CharField(max_length=255)
    master_value = models.CharField(max_length=255)
    master_key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    to_show = models.BooleanField(default=True)

    # class Meta:
    #     db_table = "tbl_master"

    def __str__(self):
        return self.title

 #-------------All Master Table End----------

 #-------------Token Master Table Start------------              

class TokenMaster(models.Model):
    user_access_token = models.CharField(max_length=255)
    user_refresh_token = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)
    user_ref = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="User Id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    to_show = models.BooleanField(default=True)

    # class Meta:
    #     db_table = "tbl_token_master"

    def __str__(self):
        return self.title

#-------------Token Master Table End------------              

#------------Role Master Table Start-----------
    
class RoleMaster(models.Model):
    
    role_name = models.CharField(max_length=255)
    role_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    to_show = models.BooleanField(default=True)

    # class Meta:
    #     db_table = "tb_role_mst"  

    def __str__(self):
        return self.title  
    
#------------Role Master Table End-----------


#-------------Category Table start-------------------

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    to_show = models.BooleanField(default=True)

    def __str__(self):
        return self.title

#--------------Category Table End---------------------


#--------------Product Table Start------------------
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_income = models.DecimalField(max_digits=10, decimal_places=2)
    validity_period = models.IntegerField()  # Assuming validity is in days
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    to_show = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
#------------Product Table End----------------------
    
#------------Wallet Table Start---------------------
    
class Wallet(models.Model):
    user_details = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    recharge_bal = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    total_income = models.DecimalField(max_digits=10, decimal_places=2)
    total_recharge = models.DecimalField(max_digits=10, decimal_places=2)
    total_assets = models.DecimalField(max_digits=10, decimal_places=2)
    total_withdrawal = models.DecimalField(max_digits=10, decimal_places=2)
    todays_income = models.DecimalField(max_digits=10, decimal_places=2)
    team_income = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    to_show = models.BooleanField(default=True)

#------------Wallet Table End---------------------
   

