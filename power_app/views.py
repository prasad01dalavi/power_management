from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files import File  # This is to save the raw file in models

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
        service = Service(project_id=1, name=new_service_data['name'],
                          mode=new_service_data['mode'])
        service.save()

        return render(request, 'power_app/service_response.html')


class GetValues(APIView):     # /get_values

    def post(self, request):
        service_id = request.data['service_id']
        values = Value.objects.filter(service_id=service_id)
        values_data = []

        for record in values:
            values_data.append({
                'name': record.name,
                'formula': record.formula
            })

        if len(values_data) == 0:
            values_data = [{'name': 'no_values'}]

        return Response(values_data)


class AddValue(APIView):     # /add_value

    def get(self, request):
        service_id = request.GET.get('id')
        context = {'service_id': service_id}
        return render(request, 'power_app/add_value.html', context)

    def post(self, request):
        new_value_data = request.data
        print(new_value_data)
        print(new_value_data['name'], type(new_value_data[
              'file']), new_value_data['service_id'])

        # destination = open('my_file.jpg', 'wb+')
        # for chunk in new_value_data['file'].chunks():
        #     destination.write(chunk)

        service = Value(service_id=new_value_data['service_id'], name=new_value_data['name'],
                        formula=new_value_data['formula'],
                        file=File(new_value_data['file']))
        service.save()

        return render(request, 'power_app/value_response.html')
