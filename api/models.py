from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RobertCategorys(models.Model):
    category_name=models.CharField(max_length=250,unique=True)

    def __str__(self) -> str:
        return self.category_name
    

    
class Manufacturers(models.Model):
    manufacturer_name=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.manufacturer_name


class Roberts(models.Model):
    robert_name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    robert_cate_name=models.CharField(max_length=250)
    manufacture_name=models.CharField(max_length=250)
    options=(
        ("INR","INR"),
        ("DOLLAR","DOLLAR"),
        ("RIYAL","RIYAL")
    )
    currency=models.CharField(max_length=100,choices=options,default="INR")
    price=models.PositiveIntegerField()
    manufacture_date=models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.robert_name
