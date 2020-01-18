from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from .springrunner import *
from threading import Thread
from rest_framework.parsers import FileUploadParser
import rest_framework.status as status


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, format='jar'):
        up_file = request.FILES['file']
        destination = open('~/oeskspring/' + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chunks are added

        # ...
        # do some stuff with uploaded file
        # ...
        return Response(up_file.name, status.HTTP_201_CREATED)


class AllMeasurementsView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, _):
        return Response(MeasurementSerializer(Measurement.objects.all(), many=True).data)

    def post(self, _):
        thread = Thread(target=create_measurement, args=('measurement-0.0.1-SNAPSHOT.jar', 4))
        thread.start()
        return Response(data=None)
