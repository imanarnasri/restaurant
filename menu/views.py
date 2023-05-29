from django.shortcuts import render

# Create your views here.

def appetizers(request):
    return render(request,'menu/appetizers.html')

def beverages(request):
    return render(request,'menu/beverages.html')

def desserts(request):
    return render(request,'menu/desserts.html')

def maincourse(request):
    return render(request,'menu/maincourse.html')

