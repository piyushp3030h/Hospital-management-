from rest_framework import serializers
from MediAccess.models import (
    CustomUser,
    Department,
    PatientRecord
)

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department

        fields = [
            'id',
            'department_name',
            'description',
        ]



class CustomUserSerializer(serializers.ModelSerializer):

    department = serializers.StringRelatedField()

    class Meta:
        model = CustomUser

        fields = [
            'id',
            'username',
            'full_name',
            'email',
            'user_type',
            'department',
            'license_number',
            'phone_number',
            'gender',
            'date_of_birth',
        ]


class PatientRecordSerializer(serializers.ModelSerializer):

    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    class Meta:
        model = PatientRecord

        fields = [
            'record_id',
            'patient',
            'doctor',
            'department',
            'diagnostics',
            'medicine_description',
            'created_at',
            'updated_at',
        ]