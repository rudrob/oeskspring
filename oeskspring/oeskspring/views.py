from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .springrunner import *
from threading import Thread

class AllMeasurementsView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, _):
        return Response(MeasurementSerializer(Measurement.objects.all(), many=True).data)

    def post(self, _):
        thread = Thread(target=create_measurement, args=('measurement-0.0.1-SNAPSHOT.jar', 4))
        thread.start()
        return Response(data = None)
