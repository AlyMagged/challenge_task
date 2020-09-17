"""inovola_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommerce.views import(
    list_available_machine_product_types,
    list_available_machine_models,
    list_available_machine_water_lines,
    list_available_pods_product_type,
    list_available_pods_flavor,
    list_available_pods_pack_size,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('machine/product_type/', list_available_machine_product_types),
    path('machine/product_model/<int:product_id>', list_available_machine_models),
    path('machine/product_type/<int:product_id>/water_line/<int:model_id>', list_available_machine_water_lines),
    path('pods/product_type/', list_available_pods_product_type),
    path('pods/product_type/pack_size/<int:product_id>', list_available_pods_flavor),
    path('pods/product_type/product_type/<int:product_id>/flavor/<int:flavor_id>', list_available_pods_pack_size),


]
