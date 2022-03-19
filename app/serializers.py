import json
from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User



# class EmployeeSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=30)
#     phone = serializers.CharField(max_length=10)

#     # defining the create method so that when serializer.save() is called a new object coming in the request body in jsonFormat is saved in the databases 
#     def create(self, validated_data):
#         print(f'create() method has been called!')
#         return Employee.objects.create(**validated_data)
#         # here **validated_data actually converts the dict into separate key value pairs i.e into keyword arguments


#     # defining the update method so that when serializer.save() is called a new object coming in the request body in jsonFormat is updated in the databases 
#     def update(self, employee, validated_data):
#         # making a new object with updated data 
#         newEmployee = Employee(**validated_data)
#         newEmployee.id = employee.id
#         newEmployee.save()
#         return newEmployee

# OR  
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['name', 'email', 'password', 'phone']
        fields = '__all__'

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     email = serializers.CharField(max_length=30)
#     username = serializers.CharField(max_length=30)
#     password = serializers.CharField(max_length=30)

# OR 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'