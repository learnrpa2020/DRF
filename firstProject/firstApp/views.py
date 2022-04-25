from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
from firstApp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def employeeView(request):
	emp={
	'id':10001,
	'name':'Monica',
	'isMarried':False,
	'salary':1252000
	}

	data=Employee.objects.all()
	response={'employees':list(data.values('name','isMarried','salary'))}
	return JsonResponse(response)

@api_view(['GET','POST'])
def employee_list(request):
	if request.method == 'GET':
		emps = Employee.objects.all()
		serializer=EmployeeSerializer(emps,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer=EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def employee_detail(request,pk):
	try:
		employee=Employee.objects.get(pk=pk)
	except Employee.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer=EmployeeSerializer(employee)
		return Response(serializer.data)

	elif request.method== 'PUT':
		serializer=EmployeeSerializer(employee,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

	elif request.method == 'DELETE':
		employee.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


