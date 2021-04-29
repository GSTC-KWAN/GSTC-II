import datetime
from django.db import models
from django.utils import timezone

# Create your models here.  

class Functions(models.Model):
    functions_text = models.CharField(max_length=200,blank=True,default='')
    pub_date=models.DateTimeField('date published')
    
    def __str__(self):
        return self.functions_text     
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
    
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Published recently'   

class Goods(models.Model):
    code=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    number=models.IntegerField(default=0)
    
    def __str__(self):
        return self.code

class Records(models.Model):
    code=models.CharField(max_length=200)
    number=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    pub_date=models.DateField('date published',auto_now_add=True)
    
    def __str__(self):
        return self.code
    
 
