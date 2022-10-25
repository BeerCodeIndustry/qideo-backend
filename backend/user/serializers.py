from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        model = User
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def get(self, validated_data):
        user = User.objects.filter(username=validated_data['username']).first()
        if user is None or (user and user.check_password(validated_data['password']) is False):
            raise AuthenticationFailed
        return user
