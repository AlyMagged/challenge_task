from django.shortcuts import render

# Create your views here.
from .models import MachineProductType


def list_available_machine_product_types(request):
    qs = MachineProductType.objects.all()
    template_name = 'machine_product_type.html'
    context = {'object_list': qs}
    return render(request, template_name, {})


def list_available_machine_models(request):
    pass


def list_available_machine_water_lines(request):
    pass


def get_machine_json(request):
    pass
