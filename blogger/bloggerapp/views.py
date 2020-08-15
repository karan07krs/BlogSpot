from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost, Contact

# Create your views here.
def index(request):
    blogs = Blogpost.objects.all();
    params = {'blogs':blogs}

    return render(request, "bloggerapp/index.html",params)

def blogpost(request,id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'bloggerapp/blogpost.html',{'post':post})

def contact(request):
    if request.method=="POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('description','')
        contact = Contact(name=name,email=email,phone=phone, desc = desc)
        contact.save()

        contacted = True
        return render(request, "bloggerapp/contact.html",{"contacted":contacted})

    return render(request, "bloggerapp/contact.html")