from django.shortcuts import render
from django.http import request as rq
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView
from .models import (
    Section,
    Item,
    Modifier
)
from .serializers import (
    SectionSerializer,
    ItemSerializer,
    ModifierSerializer,
    IndexSerializer,
    IndexItemSerializer,
    IndexModifierSerializer,
)

# Create your views here.

class Index(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = IndexSerializer

class items(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = IndexItemSerializer

class modifiers(viewsets.ModelViewSet):
    queryset = Modifier.objects.all()
    serializer_class = IndexModifierSerializer

class sectionsList(ListAPIView):
    queryset = ''
    permission_classes = []
    serializer_class = SectionSerializer

    def get(self, request):
        sections = Section.objects.all()
        serializer_class = SectionSerializer(sections, many=True)

        return Response(serializer_class.data)

class sectionsCreate(ListAPIView):
    queryset = ''
    serializer_class = ItemSerializer

    def get(self, request):
        context = {
            'message': 'Get Requests Are Not Enabled In This Path'
        }

        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        permission_classes = [IsAuthenticated]
        serializer = SectionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class itemsList(ListAPIView):
    queryset = ''
    serializer_class = ItemSerializer

    def get(self, request):
        items = Item.objects.all()
        serializer_class = ItemSerializer(items, many=True)

        return Response(serializer_class.data)

class itemsCreate(ListAPIView):
    queryset = ''
    serializer_class = ItemSerializer

    def get(self, request):
        context = {
            'message': 'Get Requests Are Not Enabled In This Path'
        }

        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        permission_classes = [IsAuthenticated]
        serializer = ItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class modifiersList(ListAPIView):
    queryset = ''
    serializer_class = ModifierSerializer

    def get(self, request):
        modifiers = Modifier.objects.all()
        serializer_class = ModifierSerializer(modifiers, many=True)

        return Response(serializer_class.data)

class modifiersCreate(ListAPIView):
    queryset = ''
    serializer_class = ModifierSerializer

    def get(self, request):
        context = {
            'message': 'Get Requests Are Not Enabled In This Path'
        }

        return Response(context, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        permission_classes = [IsAuthenticated]
        serializer = ModifierSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)