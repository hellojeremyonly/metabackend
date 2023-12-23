from rest_framework import serializers
from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


# class SingleMenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu
#         fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    booking_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'