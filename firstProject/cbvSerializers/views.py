from django.shortcuts import render
from cbvSerializers.serializers import CourseSerializer
from cbvSerializers.models import Course
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class CourseList(APIView):

	def get(self,request):
		course = Course.objects.all()
		serializer=CourseSerializer(course,many=True)
		return Response(serializer.data)


	def post(self,request):
		serializer = CourseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)


class CourseDetail(APIView):

	def get(self,request,pk):
		course=Course.objects.get(pk=pk)
		serializer=CourseSerializer(course)
		return Response(serializer.data)


	def put(self,request,pk):
		course=Course.objects.get(pk=pk)
		serializer=CourseSerializer(request,data=request.data)
		return Response(serializer.data)


	def delete(self,request,pk):
		course=Course.objects.get(pk=pk)
		course.delete()
		return Response(data='No Content')







