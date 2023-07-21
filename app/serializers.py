from rest_framework import serializers
from app.models import AddDepartment
from rest_framework import serializers
from .models import *


class AddDepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddDepartment
    fields='__all__'
    
class AddDesignationSerializer(serializers.ModelSerializer):
      
  class Meta:
    model = AddDesignation
    fields='__all__'

