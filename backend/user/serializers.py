from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        model = User

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def get(self, validated_data):
        user = User.objects.get(**validated_data)
        return user
