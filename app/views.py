from django.shortcuts import render

# Create your views here.

def Conditions(request):
    d={'a':100,'b':200}
    return render(request,'conditions.html',d)