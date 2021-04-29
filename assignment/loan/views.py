from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import Platform 
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic


import pandas as pd
import numpy as np
import gc
import json
# Create your views here.
import joblib 
from sklearn.preprocessing import StandardScaler
'''
BNB=joblib.load("loan\model.joblib")
'''

RF=joblib.load("loan\classifier.joblib")

class IndexView(generic.ListView):
    template_name='loan/index.html'
    context_object_name='latest_platform_list'
    
    def get_queryset(self):
        return Platform.objects.order_by('-pub_date')[:5]
        

class DetailView(generic.DetailView):
    model = Platform 
    template_name='loan/detail.html'
    

    
class ResultsView(generic.DetailView):
    model = Platform 
    template_name='loan/results.html'




def info(request,pk):
    ssn=get_object_or_404(Platform,pk=pk)
    name=get_object_or_404(Platform,pk=pk)
    annualincome=get_object_or_404(Platform,pk=pk)
    workingyears=get_object_or_404(Platform,pk=pk)
    if request.method == 'POST':
        ssn=request.POST.get('ssn')
        name=request.POST.get('name')
        annualincome=request.POST.get('annualincome')
        workingyears=request.POST.get('workingyears')
        predloan=0
        
    
        workingyears2=int(workingyears)
        annualincome2=int(workingyears)
        
        annualincome1=[workingyears2]
        workingyears1=[workingyears2]
        
        a=pd.DataFrame(annualincome1)
        b=pd.DataFrame(workingyears1)
        X=a.join(b,how='left',lsuffix=1)
        

        
        pred=RF.predict(X)
        
        annualincome=int(annualincome)
        
        if pred == [1]:
            predloan = 7*annualincome
        elif pred == [2]:
            predloan = 6*annualincome
        elif pred == [3]:
            predloan = 5*annualincome
        
        context={
                'ssn':ssn,
                'name':name,
                'annualincome':annualincome,
                'workingyears':workingyears,
                'pred':pred,
                'predloan':predloan,
                }
        

        return render(request,"loan/results.html",context)


     
     
     