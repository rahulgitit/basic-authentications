from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from enroll.models import testdb
from enroll.serializers import testdbserializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
class show_all_data(ModelViewSet):
    queryset=testdb.objects.all()
    serializer_class=testdbserializers
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    # permission_classes=[IsAuthenticatedOrReadOnly]
