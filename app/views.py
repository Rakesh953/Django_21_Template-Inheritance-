from django.shortcuts import render

# Create your views here.

def parent(request):
    return render(request,'parent.html')
def chield(request):
    return render(request,'chield.html')