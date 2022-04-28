from rest_framework import serializers
from mixinApp.models import CourseMixin

class MixinSerializer(serializers.ModelSerializer):
	class Meta:
		model=CourseMixin
		fields=['courseName','description','ratings']