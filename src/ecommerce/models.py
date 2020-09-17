from django.db import models

# Create your models here.


class MachineProductType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, null=True)


class MachineModel(models.Model):
    name = models.CharField(max_length=50)
    product_type_id = models.IntegerField()
    code = models.CharField(max_length=10, null=True)


class MachineWaterLine(models.Model):
    type = models.BooleanField(default=True)
    model_id = models.IntegerField()


class PodsProductType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, null=True)


class PodsFlavor(models.Model):
    name = models.CharField(max_length=50)
    product_type_id = models.IntegerField()
    code = models.CharField(max_length=10, null=True)


class PodsPackSize(models.Model):
    dozens = models.IntegerField()
    pods_flavor_id = models.IntegerField()
    code = models.CharField(max_length=10, null=True)