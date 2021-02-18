from django.shortcuts import render
from users_app.models import Users

# Create your views here.
def users(request):
    my_obj = {'users_data':Users.objects.all()}
    return render(request,'users_index_template.html',context=my_obj)