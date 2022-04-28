from django.shortcuts import render
from mixinApp.models import CourseMixin
from mixinApp.serializers import MixinSerializer
from rest_framework import generics,mixins
from rest_framework import viewsets

# Create your views here.
"""class CourseList(mixins.ListModelMixin,generics.GenericAPIView,mixins.CreateModelMixin):

	queryset = CourseMixin.objects.all()
	serializer_class=MixinSerializer

	def get(self,request):
		return self.list(request)

	def post(self,request):
		return self.create(request)

class CourseDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
	queryset=CourseMixin.objects.all()
	serializer_class=MixinSerializer

	def get(self,request,pk):
		return self.retrieve(request,pk)


	def put(self,request,pk):
		return self.update(request,pk)

	def delete(self,request,pk):
		return self.destroy(request,pk)
"""

"""class CourseList(generics.ListCreateAPIView):
	queryset = CourseMixin.objects.all()
	serializer_class=MixinSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CourseMixin.objects.all()
	serializer_class=MixinSerializer
"""

class CourseViewSet(viewsets.ModelViewSet):
	queryset = CourseMixin.objects.all()
	serializer_class=MixinSerializer
