from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .springrunner import *

class AllMeasurementsView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, _):
        create_measurement('measurement-0.0.1-SNAPSHOT.jar')
        return Response(MeasurementSerializer(Measurement.objects.all(), many=True).data)
