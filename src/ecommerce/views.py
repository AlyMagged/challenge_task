from django.shortcuts import render
from django.http import JsonResponse

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
    context = {'object_list': qs, 'product_id': product_id}
    return render(request, template_name, context)


def list_available_machine_water_lines(request, product_id, model_id):
    qs = MachineWaterLine.objects.filter(model_id=model_id)
    template_name = 'machine_water_line.html'
    context = {'object_list': qs, 'product_id': product_id, 'model_id': model_id}
    return render(request, template_name, context)


def get_machine_json(request, product_id, model_id, water_type):
    product = MachineProductType.objects.filter(id=product_id)
    product_code = product.code
    model = MachineModel.objects.filter(id= model_id)
    model_code = model.code

    sku_code = str(product_code) + str(model_code)
    response_data = {
        'sku_code': sku_code,
        'water_type': water_type,
    }
    return JsonResponse(response_data)
