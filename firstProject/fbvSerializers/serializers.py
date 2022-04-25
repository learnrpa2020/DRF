from rest_framework import serializers
from fbvSerializers.models import Passenger


class PassengerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Passenger
		fields=['firstname','lastname','travelpoints']