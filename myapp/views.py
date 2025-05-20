from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import FoodMenu
from .forms import FoodMenuForm
# Create your views here.
def home(request):
    items = FoodMenu.objects.all()
    return render(request, 'myapp/home.html', {'items':items})

def additem(request):
    form = FoodMenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('myapp:home')
    return render(request,'myapp/additemForm.html',{'form':form})

def details(request,id):
    item = FoodMenu.objects.get(pk=id)
    return render(request,'myapp/details.html',{'item':item})