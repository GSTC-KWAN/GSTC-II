from django.shortcuts import  get_object_or_404,render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Goods,Functions,Records
from django.views import generic
from django.http import Http404
from django.urls import reverse
from django.db.models import Sum,Max

# Create your views here.
class List(generic.ListView):
    template_name = 'sm/menu.html'
    context_object_name = 'latest_functions_list'
    
    def get_queryset(self):
        return Functions.objects.all()
#############################################################################  
        
class Cashier(generic.DetailView):
    model = Functions
    template_name = 'sm/cashier.html'
    
class CashResults(generic.DetailView):
    model = Functions
    template_name = 'sm/cashresults.html'

############################################################################# 

class Inventoryincrement(generic.DetailView):
    model = Functions
    template_name = 'sm/inventoryincrement.html'

class InResults(generic.DetailView):
    model = Functions
    template_name = 'sm/inresults.html'  

############################################################################# 

class Inventorydecrement(generic.DetailView):
    model = Functions
    template_name = 'sm/inventorydecrement.html'
    
class DeResults(generic.DetailView):
    model = Functions
    template_name = 'sm/deresults.html'  

############################################################################# 
    
class Inventory(generic.DetailView):
    model = Functions
    template_name = 'sm/inventory.html'
    
class StockResults(generic.DetailView):
    model = Functions
    template_name = 'sm/stockresults.html'  
    
############################################################################# 

class Retail(generic.ListView):
    model = Functions
    template_name = 'sm/retail.html'
    context_object_name = 'latest_functions_list'
    
    def get_queryset(self):
        return Functions.objects.order_by('-pub_date')[:2]
    
class Monthly(generic.DetailView):
    model = Functions
    template_name = 'sm/monthly.html'  
    
class MonthlyResults(generic.DetailView):
    model = Functions
    template_name = 'sm/monthlyresults.html'  
    
class Yearly(generic.DetailView):
    model = Functions
    template_name = 'sm/yearly.html'  
    
class YearlyResults(generic.DetailView):
    model = Functions
    template_name = 'sm/yearlyresults.html'  
    
############################################################################# 
    
  

def cash(request,pk):
    code = get_object_or_404(Goods, pk=pk)
    price = get_object_or_404(Goods, pk=pk)
    number = get_object_or_404(Goods, pk=pk)
    if request.method == 'POST':
        code=request.POST.get('code')
        price=request.POST.get('price')
        number=request.POST.get('number')
        receipts=request.POST.get('receipts')
        
        number=int(number)

        cur = Goods.objects.filter(code=code).all()
        for cur_num in cur:
             if number > cur_num.number:
                 return render(request,"sm/cashresults.html",{
                         'error_message':"IT'S NOT ENOUGH! GOTTA HAVE SOME SHIT!",
                         })
             else:
                 cur_num.number=cur_num.number-number
                 Goods.objects.filter(code=code).update(number=cur_num.number)
                 code=int(code)
                 price=int(price)
                 receipts=int(receipts)
                 receivable=price*number
                 Records.objects.create(code=code,number=number,total=receivable)
                 change=receipts-receivable
                 context={
                         'receivable':receivable,
                         'receipts':receipts,
                         'change':change,
                         }
                 return render(request,"sm/cashresults.html",context)
            
       
        
       

def increase(request,pk):
    increment=get_object_or_404(Goods, pk=pk)
    code = get_object_or_404(Goods, pk=pk)
    price = get_object_or_404(Goods, pk=pk)
    number = get_object_or_404(Goods, pk=pk)
    if request.method == 'POST':
        code=request.POST.get('code')
        price=request.POST.get('price')
        number=request.POST.get('number')
        
        cur2 = Goods.objects.filter(code=code).all()
        if cur2:
            Goods.objects.filter(code=code).update(price=price,number=number)
        else:
            Goods.objects.create(code=code,price=price,number=number)
    
    return HttpResponseRedirect(reverse('sm:inresults', args=(increment.id,)))
            
         

        
    
def decrease(request,pk):
    decrement=get_object_or_404(Goods, pk=pk)
    code = get_object_or_404(Goods, pk=pk)
    number = get_object_or_404(Goods, pk=pk)
    if request.method == 'POST':
        code=request.POST.get('code')
        number=request.POST.get('number')
        number = int(number)
        
        
        cur3=Goods.objects.filter(code=code).all()
        if cur3:
            for cur_num in cur3:
                if number > cur_num.number:
                    return render(request,"sm/deresults.html",{
                         'error_message':"YOU CANNOT DECREASE OUT OF THE STOCK!",
                         })
                else:
                    cur_num.number=cur_num.number-number
                    Goods.objects.filter(code=code).update(number=cur_num.number)
                    return HttpResponseRedirect(reverse('sm:deresults', args=(decrement.id,)))
        else:
            return render(request,"sm/deresults.html",{
                         'error_message':"YOU CANNOT EREASE THING DOESN'T EXIST!",
                         })
            
    


def stock(request,pk):
    code = get_object_or_404(Goods, pk=pk)
    if request.method == 'POST':
        code=request.POST.get('code')
        code = int(code)
        
        
        cur1 = Goods.objects.filter(code=code).all()
        if cur1:
            for cur_number in cur1:
                if cur_number.number < 60:
                    return render(request,"sm/stockresults.html",{'error_message':"Go get some products here!",})
                else:
                    show=Goods.objects.filter(code=code).all()
                    return render(request,"sm/stockresults.html",{'show':show,'code':code,}) 
        else:
            return render(request,"sm/stockresults.html",{'error_message':"No such product here!",})
        
        
     
def month(request,pk):
    if request.method == 'POST':
        month=request.POST.get('month')
        time=Records.objects.filter(pub_date__month=month).values('code').all()
        if time:
            bsv = Records.objects.filter(pub_date__month=month).values('code').annotate(num=Sum("number")).aggregate(number2=Max('num'))
            bsv=bsv['number2']
            bs = Records.objects.filter(pub_date__month=month).values('code').annotate(number=Sum("total")).aggregate(number2=Max('number'))
            bs = bs['number2']
            vgs = Records.objects.filter(pub_date__month=month).values('code').annotate(number=Sum("total"))
            totalsales= Records.objects.filter(pub_date__month=month).aggregate(total=Sum('total'))
            ts=totalsales['total']
            return render(request,"sm/monthlyresults.html",{'bsv':bsv,'bs':bs,'vgs':vgs,'ts':ts,})  
        else:
            return render(request,"sm/monthlyresults.html",{'error_message':"No such Month Statistics here!",})
        
        
def year(request,pk):
    if request.method == 'POST':
        year=request.POST.get('year')
        time=Records.objects.filter(pub_date__year=year).values('code').all()
        if time:
            bsv = Records.objects.filter(pub_date__year=year).values('code').annotate(num=Sum("number")).aggregate(number2=Max('num'))
            bsv=bsv['number2']
            bs = Records.objects.filter(pub_date__year=year).values('code').annotate(number=Sum("total")).aggregate(number2=Max('number'))
            bs = bs['number2']
            vgs = Records.objects.filter(pub_date__year=year).values('code').annotate(number=Sum("total"))
            totalsales= Records.objects.filter(pub_date__year=year).aggregate(total=Sum('total'))
            ts=totalsales['total']
            return render(request,"sm/yearlyresults.html",{'bsv':bsv,'bs':bs,'vgs':vgs,'ts':ts,})  
        else:
            return render(request,"sm/yearlyresults.html",{'error_message':"No such Year Statistics here!",})
        
        
    
    
    
       
        
    

    

    
    
  
    



