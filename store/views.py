from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    authentication,
    permissions,
    status,
    pagination,
)

from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Category, Subcategory, Item
from .serializers import ItemProductSerializer


class ProductAPI(APIView):
    """
    returns list of
    {name: str
    category: str
    subcategory:str 
    amount:int}

    exception:
    returns 400 status
    """

    def get(self, request, format=None):

        query_params = ['category', 'subcategory', 'name']
        print(list(request.query_params.keys()))
        if list(request.query_params.keys()) not in query_params:
            return Response( {"Not allowed"}, status=status.HTTP_403_FORBIDDEN)

        category = request.query_params.get('category', None)
        subcategory = request.query_params.get('subcategory', None)
        name = request.query_params.get('name', None)

        if name:
            serializer_class = ItemProductSerializer
            try:
                queryset = Item.objects.get(name = name)
                print("i am executed")
            except:
                return Response( {"Item does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            serialized_data = serializer_class(queryset, many=True)
            return Response(serialized_data.data)


        elif subcategory:
            serializer_class = ItemProductSerializer
            try:
                queryset = Subcategory.objects.get(name=subcategory).itemsInSubcategory.all()
            except:
                    return Response( {"Subcategory does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            serialized_data = serializer_class(queryset, many=True)
            return Response(serialized_data.data)


        elif category:
            serializer_class = ItemProductSerializer
            try:
                subcategory_id_list = Category.objects.get(name=category).subcategoriesInCategory.values_list("id", flat=True)
                queryset = Item.objects.filter(subcategory__in = subcategory_id_list)

            except:
                return Response( {"Category does not exist"}, status=status.HTTP_400_BAD_REQUEST)

            serialized_data = serializer_class(queryset, many=True)
            return Response(serialized_data.data)


        else:
            serializer_class = ItemProductSerializer
            try:   
                queryset = Item.objects.all()
            except:
                return Response( {"zero items were found in the database"}, status=status.HTTP_400_BAD_REQUEST)
            
            serialized_data = serializer_class(queryset, many=True)
            return Response(serialized_data.data)

        
