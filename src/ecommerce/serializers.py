'''
from rest_framework import serializers
from .models import MachineModel, MachineProductType, MachineWaterLine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Tutorial
        fields = (MachineProductType().code,
                  MachineModel().code,
                  )
'''