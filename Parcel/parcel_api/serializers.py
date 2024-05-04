from rest_framework import serializers
from .models import Parcel

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = ['name','parcel_id','mobile_number','status']
