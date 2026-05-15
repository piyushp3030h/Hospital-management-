from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from MediAccess.models import (
    CustomUser,
    Department,
    PatientRecord
)

from .serializers import (
    CustomUserSerializer,
    DepartmentSerializer,
    PatientRecordSerializer
)



@api_view(['GET'])
def get_routes(request):

    routes = [

        # JWT
        'POST /api/token/',
        'POST /api/token/refresh/',

        # Departments
        'GET /api/departments/',
        'GET /api/departments/<id>/',

        # Patients
        'GET /api/patients/',
        'GET /api/patients/<id>/',

        # Records
        'GET /api/records/',
        'GET /api/records/<id>/',
    ]

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_departments(request):

    departments = Department.objects.all()

    serializer = DepartmentSerializer(
        departments,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_department(request, pk):

    department = get_object_or_404(
        Department,
        id=pk
    )

    serializer = DepartmentSerializer(
        department,
        many=False
    )

    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patients(request):

    patients = CustomUser.objects.filter(
        user_type='patient'
    )

    serializer = CustomUserSerializer(
        patients,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient(request, pk):

    patient = get_object_or_404(
        CustomUser,
        id=pk,
        user_type='patient'
    )

    serializer = CustomUserSerializer(
        patient,
        many=False
    )

    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_records(request):

    records = PatientRecord.objects.all()

    serializer = PatientRecordSerializer(
        records,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_record(request, pk):

    record = get_object_or_404(
        PatientRecord,
        record_id=pk
    )

    serializer = PatientRecordSerializer(
        record,
        many=False
    )

    return Response(serializer.data)