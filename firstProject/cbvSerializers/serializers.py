from rest_framework import serializers
from cbvSerializers.models import Course


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Course
		fields=['name','description','ratings']