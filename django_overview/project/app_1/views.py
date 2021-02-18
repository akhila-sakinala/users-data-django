from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import Topic,Webpage,AccessRecord

# Create your views here.


def index(request):
    return HttpResponse('Hello world!')

def hello(request):
    return HttpResponse('Here is a hello response')

def howAreYou(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'index.html',context=date_dict)