from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from .models import (
    MachineProductType,
    MachineModel,
    MachineWaterLine,
    PodsProductType,
    PodsFlavor,
    PodsPackSize,
)


def list_available_machine_product_types(request):
    qs = MachineProductType.objects.all()
    codes = []
    for obj in qs:
        product_code = obj.code
        product_id = obj.id
        qs2 = MachineModel.objects.filter(product_type_id=product_id)
        for row in qs2:
            model_code = row.code
            model_id = row.id
            codes.append(product_code + model_code)
    json_data = {
        'SKU': codes
    }
    return JsonResponse(json_data)


def list_available_machine_models(request, product_id):
    model_qs = MachineModel.objects.filter(product_type_id=product_id)
    product_qs = MachineProductType.objects.filter(id=product_id)
    codes = []
    for product_object in product_qs:
        for model_object in model_qs:
            codes.append(product_object.code + model_object.code)
    json_data = {
        'SKU': codes
    }
    return JsonResponse(json_data)


def list_available_machine_water_lines(request, product_id, model_id):
    model_qs = MachineModel.objects.filter(id=model_id)
    product_qs = MachineProductType.objects.filter(id=product_id)
    water_qs = MachineWaterLine.objects.filter(model_id=model_id)
    codes = []
    water_lines = []
    dic = {}
    for product_object in product_qs:
        for model_object in model_qs:
            code = product_object.code + model_object.code
            codes.append(code)
            for water_object in water_qs:
                water_lines.append(water_object.type)
            dic[code] = water_lines
            water_lines = []
    json_data = {
        'SKU': dic
    }
    return JsonResponse(json_data)

'''
def get_machine_json(request, product_id, model_id, water_type):
    product = MachineProductType.objects.filter(id=product_id)
    product_code = product.code
    model = MachineModel.objects.filter(id=model_id)
    model_code = model.code

    sku_code = str(product_code) + str(model_code)
    response_data = {
        'sku_code': sku_code,
        'water_type': water_type,
    }
    return JsonResponse(response_data)
'''


# Pods code : (product type, pack size, coffee flavor)
def list_available_pods_product_type(request):
    product_qs = PodsProductType.objects.all()
    codes = []
    for product_object in product_qs:
        product_id = product_object.id
        flavor_qs = PodsFlavor.objects.filter(product_type_id=product_id)
        for flavor_object in flavor_qs:
            flavor_id = flavor_object.id
            pack_size_qs = PodsPackSize.objects.filter(pods_flavor_id=flavor_id)
            for pack_size_object in pack_size_qs:
                codes.append(product_object.code + pack_size_object.code + flavor_object.code)
    json_data = {
        'SKU': codes
    }
    return JsonResponse(json_data)


# Pods code : (product type, pack size, coffee flavor)
def list_available_pods_flavor(request, product_id):
    codes = []
    product_object = PodsProductType.objects.get(id=product_id)
    # product_object = product_qs[0]
    product_code = product_object.code
    flavor_qs = PodsFlavor.objects.filter(product_type_id=product_id)
    for flavor_object in flavor_qs:
        flavor_id = flavor_object.id
        pack_size_qs = PodsPackSize.objects.filter(pods_flavor_id=flavor_id)
        for pack_size_object in pack_size_qs:
            codes.append(product_code + pack_size_object.code + flavor_object.code)

    json_data = {
        'SKU': codes
    }

    return JsonResponse(json_data)


# Pods code : (product type, pack size, coffee flavor)
def list_available_pods_pack_size(request, product_id, flavor_id):
    codes = []

    product_object = PodsProductType.objects.get(id=product_id)
    product_code = product_object.code

    flavor_object = PodsFlavor.objects.get(id=flavor_id)
    flavor_code = flavor_object.code

    pack_size_qs = PodsPackSize.objects.filter(pods_flavor_id=flavor_id)
    for pack_size_object in pack_size_qs:
        pack_size_code = pack_size_object.code
        codes.append(product_code + pack_size_code + flavor_code)

    json_data = {
        'SKU': codes
    }

    return JsonResponse(json_data)