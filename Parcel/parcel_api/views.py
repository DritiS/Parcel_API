from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Parcel
from .serializers import ParcelSerializer

class ParcelTracking(APIView):
    def get(self, request, parcel_id):
        try:
            parcel = Parcel.objects.get(parcel_id=parcel_id)
            serializer = ParcelSerializer(parcel)
            return Response(serializer.data)
        except Parcel.DoesNotExist:
            return Response({"message":"Parcel not found"},status=status.HTTP_404_NOT_FOUND)