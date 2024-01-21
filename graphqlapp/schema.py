import strawberry

from typing import List
from .models import Doctor
from .types import DoctorType


# Query
# GET


@strawberry.type
class Query:
    @strawberry.field
    def doctors(
        self, name: str = None
    ) -> List[DoctorType]:  # Defines return data
        if name:  # if name is provided
            doctor = Doctor.objects.filter(name=name)
            return doctor
        return Doctor.objects.all()  # if name is not provided


# Mutation
# Create, Update, Delete (POST, PUT, PATCH, DELETE)


@strawberry.type
class Mutation:
    @strawberry.field
    def create_doctor(self, name: str, address: str, specialty: str) -> DoctorType:
        doctor = Doctor(name=name, address=address, specialty=specialty)
        doctor.save()
        return doctor

    @strawberry.field
    def update_doctor(
        self, id: int, name: str, address: str, specialty: str
    ) -> DoctorType:
        doctor = Doctor.objects.get(id=id)
        doctor.name = name
        doctor.address = address
        doctor.specialty = specialty
        doctor.save()
        return doctor

    @strawberry.field
    def delete_doctor(self, id: int) -> DoctorType:
        doctor = Doctor.objects.get(id=id)
        doctor.delete()


# Define a Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
