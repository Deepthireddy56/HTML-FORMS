from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def htmlforms(request):
    if request.method=='POST':
        return HttpResponse('Data is successfully submitted......')

    return render(request,'htmlforms.html')