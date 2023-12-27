from django.shortcuts import render
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.obejcts.all()
        serializer= StudentSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.error, status=status.HTTP_404_NOT_FOUND)
    
    def retrive(self, request, pk=None):
        obj = get_object_or_404(Student, pk = pk)
        serializer = StudentSerializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk = None):
        obj = get_object_or_404(Student, pk = pk)
        serializer = StudentSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.error, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk = None):
        obj = get_object_or_404(Student, pk = pk)
        serializer = StudentSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.error, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk = None):
        obj = get_object_or_404(Student, pk = pk)
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)