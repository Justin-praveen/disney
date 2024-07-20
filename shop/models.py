from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    des=models.CharField(max_length=500)
    category_image=models.ImageField(upload_to="images/")
    status=models.BooleanField(default=True)
    cate_code=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Product (models.Model):
    key=models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    p_code=models.IntegerField(null=True,blank=True)
    status=models.BooleanField(default=True)
    product_des=models.CharField(max_length=500)
    product_image=models.ImageField(upload_to="images/")
    old_price=models.IntegerField()
    new_price=models.IntegerField()
    seller=models.CharField(max_length=100)
    trend=models.BooleanField(default=False)
    rating=models.FloatField()
    cate_code=models.IntegerField(null=True,blank=True)
    arrival=models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name
    
class New_Arrival (models.Model):
    key=models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    p_code=models.IntegerField(null=True,blank=True)
    status=models.BooleanField(default=True)
    product_des=models.CharField(max_length=500)
    product_image=models.ImageField(upload_to="images/")
    old_price=models.IntegerField()
    new_price=models.IntegerField()
    seller=models.CharField(max_length=100)
    trend=models.BooleanField(default=False)
    rating=models.FloatField()
    cate_code=models.IntegerField(null=True,blank=True)
    arrival=models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.product_name

class FAQ (models.Model):
    q_code=models.IntegerField(null=True,blank=True)
    question=models.CharField( max_length=100)
    answer=models.CharField( max_length=500)
    p_code=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.question
    
class Logins (models.Model):
    username=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    type=models.CharField( max_length=50)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
    
class Orders (models.Model):
    p_code=models.IntegerField(null=True,blank=True)
    name=models.CharField( max_length=100)
    image=models.ImageField(upload_to="images/")
    username=models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    
class Cart (models.Model):
    p_code=models.IntegerField(null=True,blank=True)
    name=models.CharField( max_length=50)
    username=models.CharField( max_length=50)
    price=models.IntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True)
    
    def __str__(self):
        return self.name