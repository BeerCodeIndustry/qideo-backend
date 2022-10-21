from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        model = User
