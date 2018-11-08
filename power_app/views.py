from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Project, Service, Value
import json

# Create your views here.


def index(request):    # /index
    services = Service.objects.all()
    service_data = []
    for record in services:
        service_data.append({
            'project': record.project.name,
            'name': record.name,
            'mode': record.mode
        })
    context = {"services": json.dumps(service_data),
               "services_count": json.dumps(len(service_data))}
    return render(request, 'power_app/index.html', context)


class AddService(APIView):     # /add_service

    def get(self, request):
        return render(request, 'power_app/add_service.html')

    def post(self, request):
        new_service_data = request.data
        print(new_service_data['name'])
        service = Service(project_id=1, name=new_service_data['name'],
                          mode=new_service_data['mode'])
        service.save()

        return Response("Success")
