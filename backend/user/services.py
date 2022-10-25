from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class AuthUserService:
    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @staticmethod
    def generate_response(data, tokens, status, headers=None):
        response = Response(
            data,
            status=status,
            headers=headers
        )
        response.set_cookie('access', tokens['access'])
        response.set_cookie('refresh', tokens['refresh'])
        return response
