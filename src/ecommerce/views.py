from django.shortcuts import render

# Create your views here.
from .models import MachineProductType, MachineModel, MachineWaterLine


def list_available_machine_product_types(request):
    qs = MachineProductType.objects.all()
    template_name = 'machine_product_type.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def list_available_machine_models(request, product_id):
    qs = MachineModel.objects.filter(product_type_id=product_id)
    template_name = 'machine_models.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def list_available_machine_water_lines(request, model_id):
    qs = MachineWaterLine.objects.filter(model_id=model_id)
    template_name = 'machine_water_line.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def get_machine_json(request):
    pass
