from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import ShoppingMalls
# Create your views here.
# def index(request):
#     feature1 = Feature()
#     feature1.id = 0
#     feature1.name = 'Fast'
#     feature1.is_t = True
#     feature1.details = 'This is very fast'
#     features = [feature1]
#     for feature in features:
#         pass
#     return render(request,'index.html',{'features':features})

def index(request):
    mall_list = ShoppingMalls.objects.all()
    return render(request,'index.html',{'mall_lists':mall_list})

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
        shopping_mall_name = request.POST['mall_name']
        category_1 = request.POST['product1']
        category_2 = request.POST['product2']
        category_3 = request.POST['product3']
        category_4 = request.POST['product4']
        category_5 = request.POST['product5']
        category_6 = request.POST['product6']
        category_7 = request.POST['product7']
        # here gmail = link1 = request.POST['link3']
        link1 = request.POST['link3']
        # website_link
        link2 = request.POST['link1']
        # facebook_link
        link3 = request.POST['link2']
        # other link
        link4 = request.POST['link4']
        # area = division
        division = request.POST['division']
        # address = location
        location = request.POST['location']
        
        phone_1 = request.POST['phone1']
        phone_2 = request.POST['phone2']
        phone_3 = request.POST['phone3']
        phone_4 = request.POST['phone4']
        
        image_0 = request.POST['image_0']
        image_1 = request.POST['image_1']
        image_2 = request.POST['image_2']
        image_3 = request.POST['image_3']
        image_4 = request.POST['image_4']
        # description = mall_description
        mall_description = request.POST['mall_description']
        
        facilities_1 = request.POST['facilities_1']
        facilities_2 = request.POST['facilities_2']
        facilities_3 = request.POST['facilities_3']
        facilities_4 = request.POST['facilities_4']
        facilities_5 = request.POST['facilities_5']
        facilities_6 = request.POST['facilities_6']
        facilities_7 = request.POST['facilities_7']
        facilities_8 = request.POST['facilities_8']
        facilities_9 = request.POST['facilities_9']
        facilities_10 = request.POST['facilities_10']
        facilities_11 = request.POST['facilities_11']
        facilities_12 = request.POST['facilities_12']
        facilities_13 = request.POST['facilities_13']
        facilities_14 = request.POST['facilities_14']
        facilities_15 = request.POST['facilities_15']
        
        floors_1 = request.POST['floors_1']
        floors_2 = request.POST['floors_2']
        floors_3 = request.POST['floors_3']
        floors_4 = request.POST['floors_4']
        floors_5 = request.POST['floors_5']
        floors_6 = request.POST['floors_6']
        floors_7 = request.POST['floors_7']
        floors_8 = request.POST['floors_8']
        floors_9 = request.POST['floors_9']
        floors_10 = request.POST['floors_10']
        floors_11 = request.POST['floors_11']
        floors_12 = request.POST['floors_12']

        shoppingMalls = ShoppingMalls.objects.create(shopping_mall_name =shopping_mall_name,description=mall_description,address=location,category_1=category_1,category_2=category_2,category_3=category_3,category_4=category_4,category_5=category_5,category_6=category_6,category_7=category_7,gmail_link=link1,website_link=link2,facebook_link=link3,other_link=link4,phone_1=phone_1,phone_2=phone_2,phone_3=phone_3,phone_4=phone_4,facilities_1=facilities_1,facilities_2=facilities_2,facilities_3=facilities_3,facilities_4=facilities_4,facilities_5=facilities_5,facilities_6=facilities_6,facilities_7=facilities_7,facilities_8=facilities_8,facilities_9=facilities_9,facilities_10=facilities_10,facilities_11=facilities_11,facilities_12=facilities_12,facilities_13=facilities_13,facilities_14=facilities_14,facilities_15=facilities_15,floors_1=floors_1,floors_2=floors_2,floors_3=floors_3,floors_4=floors_4,floors_5=floors_5,floors_6=floors_6,floors_7=floors_7,floors_8=floors_8,floors_9=floors_9,floors_10=floors_10,floors_11=floors_11,floors_12=floors_12,division=division,image_0=image_0,image_1=image_1,image_2=image_2,image_3=image_3,image_4=image_4)
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
