from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import ShoppingMalls

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_t = True
    feature1.details = 'This is very fast'
    features = [feature1]
    for feature in features:
        pass
    return render(request,'index.html',{'features':features})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if  User.objects.filter(email=email).exists():
                messages.info(request,'Email Already in use!!!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already Exists!!!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password not same')
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Credential Invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    posts = [1,2,3,4,5,'tim','tom','john']
    return render(request,'counter.html',{'posts': posts})

def post(request,pk):
    return render(request,'post.html',{'pk': pk})
def add_malls(request):
    if  request.method == 'POST':
        mallname = request.POST['mall_name']
        product1 = request.POST['product1']
        product2 = request.POST['product2']
        product3 = request.POST['product3']
        product4 = request.POST['product4']
        product5 = request.POST['product5']
        product6 = request.POST['product6']
        product7 = request.POST['product7']
        link1 = request.POST['link1']
        link2 = request.POST['link2']
        # gmail = link3
        link3 = request.POST['link3']
        link4 = request.POST['link4']
        division = request.POST['division']
        location = request.POST['location']

        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        phone3 = request.POST['phone3']
        phone4 = request.POST['phone4']
        images = request.POST['images']
        mall_description = request.POST['mall_description']
        # if ShoppingMalls.objects.filter(mall_name=mall_name).exist():
        #     messages.info(request,'Mall name already Exist!!!')
        #     return redirect('add_malls')
        # elif ShoppingMalls.objects.filter(link1=link1).exists():
        #     messages.info(request,'Websites already exist!!!')
        #     return redirect('add_malls')
        # elif ShoppingMalls.objects.filter(link2=link2).exists():
        #     messages.info(request,'Facebook link already exist!!!')
        #     return redirect('add_malls')
        # elif ShoppingMalls.objects.filter(link3=link3).exists():
        #     messages.info(request,'Gmail already exist!!!')
        #     return redirect('add_malls')
        # elif ShoppingMalls.objects.filter(link4=link4).exists():
        #     messages.info(request,'Link already exist!!!')
        #     return redirect('add_malls')
        # elif ShoppingMalls.objects.filter(phone1=phone1).exists():
        #     messages.info(request,'Number already exist!!!')
        #     return redirect('add_malls')
        # else:
        shoppingMalls = ShoppingMalls.objects.create(mallname=mallname, product1=product1,product2=product2,product3=product3,product4=product4,product5=product5,product6=product6,product7=product7,link1=link1,link2=link2,link3=link3,link4=link4,division=division,location=location,phone1=phone1,phone2=phone2,phone3=phone3,phone4=phone4,images=images,mall_description=mall_description)
        shoppingMalls.save();
        return redirect('/')

    else:
        messages.info(request,'something went wrong')
        return render(request,'add_malls.html')














def shops(request):
    return render(request,'shops.html')
def brands(request):
    return render(request,'brand.html')
def about(request):
    return render(request,'about.html')
def brand_details(request):
    return render(request,'brand_details.html')
def shop_details(request):
    return render(request,'shop_details.html')

def add_brands(request):
    return render(request,'add_brands.html')
