from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse 

# Create your views here.
def firstRender(request):
    return render(request,'home.html')

def firstRender1(request):
    return HttpResponse('''<h1>Hello....Rahul</h1>''')

def firstRender2(request):
    data={
        'name':'Rahul Lokhande',
        'age':24,
        'adress':"Ashoka Garden Bhopal M.P."
    }
    return JsonResponse(data)

def firstRender3(request):
    return redirect("https://in.pinterest.com/")