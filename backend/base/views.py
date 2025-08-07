from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.products import products


@api_view(["GET"])
def getRoutes(request):
    return Response("Hello")


@api_view(["GET"])
def getProducts(request):
    return Response(products)


@api_view(["GET"])
def getProduct(request, pk):
    product = None

    for p in products:
        if p["_id"] == pk:
            product = p
            break

    return Response(product)
