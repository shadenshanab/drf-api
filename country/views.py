from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers  import CountrySerializer

from .models import Country


class CountryListView(ListCreateAPIView):
    queryset= Country.objects.all()
    serializer_class= CountrySerializer


class CountryDetailView(RetrieveUpdateDestroyAPIView):
    queryset= Country.objects.all()
    serializer_class= CountrySerializer
