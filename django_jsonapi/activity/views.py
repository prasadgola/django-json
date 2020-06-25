from django.shortcuts import render
from activity.models import User, ActivityPeriod
from activity.serializers import UserSerializer, ActivityPeriodSerializer
from rest_framework import viewsets

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer