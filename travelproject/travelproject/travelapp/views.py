from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import meet
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=meet.objects.all()
    return render(request,"index.html",{'result':obj, 'res1':obj1})
