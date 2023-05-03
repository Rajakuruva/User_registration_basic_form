from django.shortcuts import render
from django.http import *
from app.forms import *
# Create your views here.

def Registration(request):
    d={'UO':Userform(),'PO':Profileform()}
    if request.method=='POST' and request.FILES:
        USO=Userform(request.POST)
        POS=Profileform(request.POST,request.FILES)
        if USO.is_valid() and POS.is_valid():
            NUSO=USO.save(commit=False)
            NUSO.set_password(USO.cleaned_data['password'])
            NUSO.save()
            NPOS=POS.save(commit=False)
            NPOS.username=NUSO
            NPOS.save()
            return HttpResponse("Data inserted data!!")
        else:
            return HttpResponse("Invalid data")
    return render(request,'Registration.html',d)