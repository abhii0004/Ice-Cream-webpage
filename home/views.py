from django.shortcuts import render, HttpResponse
from home.models import Contact

def index(request):
    context= {
        'variable1':"HELLO WORLD"
    }
    return render(request, 'index.html', context)

# def index(request):
#     return HttpResponse("This is first project of django")
# Create your views here.

def service(request):
   return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc= desc)
        contact.save()
    return render(request, 'contact.html')

