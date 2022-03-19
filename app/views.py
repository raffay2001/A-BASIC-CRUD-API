import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer, UserSerializer
from app import serializers
from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @csrf_exempt
@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        # return JsonResponse(serializer.data, safe = False)
        return Response(serializer.data)
    elif request.method == 'POST':
        # jsonData = JSONParser().parse(request)      # returns the posted Json Object.
        # serializer = EmployeeSerializer(data=jsonData)
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()           # it calls the create() method in EmployeeSerializer    
                                        # class
            # return JsonResponse(serializer.data, safe=False)
            return Response(serializer.data)
        else:
            # return JsonResponse(serializer.errors, safe=False)
            return Response(serializer.data)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def employeeDetailView(request, pk):
    try:
        # Accessing the Employee object with the primary key 
        employee = Employee.objects.get(pk=pk)
        print(employee)
       
    except Employee.DoesNotExist:
        # return HttpResponse(status=404, )
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        # deleting the employee if its a delete request 
        employee.delete()
        # return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        # getting a specific employee from the employee's id
        serializer = EmployeeSerializer(employee)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # updating the employee with the given id
        # jsonData = JSONParser().parse(request)   { instead of using JSONParser().parse(request) we can also use { request.data } which automatically parses the posted JSON objects }
        # serializer = EmployeeSerializer(employee, data=jsonData)
        # or 
        serializer = EmployeeSerializer(employee, data=request.data)
        
        # checking if the posted JSON Oject is valid or not 
        if serializer.is_valid():
            serializer.save()           # it calls the update() method in EmployeeSerializer    
                                        # class
            # return JsonResponse(serializer.data, safe=False)
            return Response(serializer.data)
        
        # if the posted data is not valid then 
        else:
            # return JsonResponse(serializer.errors, safe=False)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def userListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return Response(serializer.data)