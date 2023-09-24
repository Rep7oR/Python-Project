from django.shortcuts import render

from.models import table
from.models import team
# Create your views here.
def home(request):
    obj = table.objects.all()
    team_pic = team.objects.all()
    return render(request, 'index.html', {'image': obj, 'team_pic': team_pic})

def index(request):
    obj = table.objects.all()
    team_pic = team.objects.all()
    return  render(request,'index.html',{'image': obj, 'team_pic': team_pic})


def about(request):
    return render(request,'index.html')

