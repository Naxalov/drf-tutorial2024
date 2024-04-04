from django.shortcuts import render
from django.views import View

from django.http import HttpResponse,JsonResponse
from rest_framework import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

class Index(View):
    def get(self, request):
        task = Task.objects.first()
        serializer = TaskSerializer(task)
        data = serializer.data
        return JsonResponse(data)


class AddTask(View):
    def post(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")
    

@api_view(['GET'])
def home(request: request):
    print(request)
    print(request.query_params)
    data = {
        "message": "Hello, world. You're at the polls index."
    }
    return Response(data,status=status.HTTP_200_OK)
    