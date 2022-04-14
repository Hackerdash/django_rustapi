from django.http import HttpResponse
from django.shortcuts import render
from .models import Name_task
from .serializers import taskSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getdata(request):
    tasks=Name_task.objects.all()
    seriali=taskSerializer(tasks, many=True)
    print(seriali)
    json_data=JSONRenderer().render(seriali.data)
    return HttpResponse(json_data)

@api_view(['POST'])
def postdata(request):
    data = request.POST.get('task')
    name_task=Name_task(name=data)
    name_task.save()
    return HttpResponse(name_task)

def home(request):
    return render(request,'index.html')