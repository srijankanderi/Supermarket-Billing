from rest_framework import viewsets 
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

from .serializers import *


class ProductAPI(APIView):
    """
    returns 
    {name: str
    category: str
    subcategory:str 
    amount:int}

    exception:
    returns 400 status
    """
    def get(self, request, format=None):
        category = request.query_params.get('category', None)
        subcategory = request.query_params.get('subcategory', None)
        name = request.query_params.get('name', None)

        if category:
            serializer_class = ProductCategorySerializer
            if subcategory:
                serializer_class = ProductSubcategorySerializer
                if name:
                    serializer_class = ItemProductSerializer
            ##fix this 
            queryset = Category.objects.get.all()
            serialized_data = serializer_class(queryset, many=True)
            return Response(serialized_data.data)


        if subcategory:
            serializer_class = ProductSubcategorySerializer
            if name:
                serializer_class = ItemProductSerializer
            
            ##fix this 
            queryset = Subcategory.objects.all()
            serialized_data = serializer_class(queryset, many=True)
            return Response(serialized_data.data)


        if name:
            serializer_class = ItemProductSerializer

            ##fix this 
            queryset = Item.objects.all()
            serialized_data = serializer_class(queryset, many=True)
            return Response(serialized_data.data)
            # case3

        
