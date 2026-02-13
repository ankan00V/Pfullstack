from django.http import HttpResponse
from django.shortcuts import render

def LPU(request):
    return render(request, 'index.html')

def about(req):
    return HttpResponse("wowowowow")
