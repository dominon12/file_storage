from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from . import models, serializers


class ImageListOrCreate(APIView):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ImageDetailOrDelete(APIView):
    serializer_class = serializers.ImageSerializer

    def get(self, request, pk, *args, **kwargs):
        image = get_object_or_404(models.Image, pk=pk)
        serializer = self.serializer_class(instance=image)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        image = get_object_or_404(models.Image, pk=pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



