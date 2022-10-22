from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins, status

from .models import User
from .mixins import SerializerMappingMixin
from .serializers import UserSerializer, LoginUserSerializer
from .services import AuthUserService


class AuthUserViewSet(
    SerializerMappingMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer = UserSerializer
    serializer_mapping = {
        'login': LoginUserSerializer
    }

    @action(detail=False, methods=['POST'])
    def registration(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            AuthUserService.get_tokens_for_user(serializer.instance),
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get(serializer.validated_data)
        return Response(
            AuthUserService.get_tokens_for_user(user),
            status=status.HTTP_200_OK,
        )
