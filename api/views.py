from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Action
from .serializers import UserProfile, UserAction, ActionSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# Create your views here.


class UserProfileViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserProfile


class CreateAction(ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


