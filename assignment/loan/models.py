from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Platform(models.Model):
    platform_text = models.CharField(max_length=200)
    #the name of loan platform
    pub_date=models.DateTimeField('date published')
    #the date of platform publishing
    ssn=models.CharField(max_length=200)
    #the description of ssn
    name=models.CharField(max_length=200)
    #the description of name
    annualincome=models.CharField(max_length=200)
    #the description of annual income
    workingyears=models.CharField(max_length=200)  
    #the description of working years
    pred=models.CharField(max_length=200)
    predloan=models.CharField(max_length=200) 
    
    def __str__(self):
        return self.platform_text    
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_description='Published recently'

        


    
    
'''
class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    #the matching question with the choice
    choice_text=models.CharField(max_length=200)
    #the description of choices
    
    def __str__(self):
        return self.choice_text
'''