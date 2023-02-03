from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from students.serializers import StudentSerializer
from students.models import Student
from courses.serializers import CourseSerializer,AttendanceSerializer
from courses.models import Course,Attendance
# Create your views here.


class StudentAPI(APIView):
    def get(self, request):
        query = Student.objects.all()
        serializer = StudentSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class=AttendanceSerializer
    queryset=Attendance.objects.all()
class CourseAPI(APIView):
    def get(self, request):
        query = Course.objects.all()
        serializer = CourseSerializer(query, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)