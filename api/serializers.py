from rest_framework import serializers
from .models import UserAction, Action
from django.contrib.auth import get_user_model
from account.models import User


class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = "__all__"


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"
