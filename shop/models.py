from django.db import models

# Create your models here.
class products(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=50,default="") 
    subcategory = models.CharField(max_length=50,default="")
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="shop/imges",default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name