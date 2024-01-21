import strawberry

from typing import List
from . import models


@strawberry.django.type(models.Doctor)
class DoctorType:
    id: int
    name: str
    name: str
    address: str
