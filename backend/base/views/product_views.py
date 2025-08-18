from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Product
from base.serializers import ProductSerializer


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(instance=products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    product = get_object_or_404(Product, _id=pk)
    serializer = ProductSerializer(instance=product)
    return Response(serializer.data)
