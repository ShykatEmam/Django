from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

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

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount': amount_of_words})