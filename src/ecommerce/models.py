from django.db import models

# Create your models here.


class MachineProductType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, null=True)

    def get_available_models(self):
        product_type_id = self.id
        qs = MachineModel.objects.filter(product_type_id=product_type_id)
        return qs


class MachineModel(models.Model):
    name = models.CharField(max_length=50)
    product_type_id = models.IntegerField()
    code = models.CharField(max_length=10, null=True)

    def get_available_water_line(self):
        model_id = self.id
        qs = MachineWaterLine.objects.filter(model_id=model_id)
        return qs


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