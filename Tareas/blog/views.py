from django.shortcuts import render

def elemento1(request):
    return render(request,'blog/elemento1.html',{})
