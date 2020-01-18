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

    # def get_queryset(self):
    #     queryset = Measurement.objects.all()
    #     namespace = self.request.query_params.get('namespace')
    #     if namespace:
    #         queryset = queryset.filter(namespace=namespace)
    #     return queryset

    def get(self, request):
        namespace = request.query_params.get('namespace')
        return Response(MeasurementSerializer(
            Measurement.objects.filter(namespace=namespace), many=True).data)

    def post(self, request):
        data = request.data
        jarname = data['jarname']
        times = data['times']
        namespace = data['namespace']
        if jarname is None:
            raise serializers.ValidationError("Missing jarname param")
        if times is None:
            raise serializers.ValidationError("Missing times param")
        if namespace is None:
            raise serializers.ValidationError("Missing namespace param")
        thread = Thread(target=create_measurement,
                        args=(jarname, times, namespace))
        thread.start()
        return Response(data=None)
