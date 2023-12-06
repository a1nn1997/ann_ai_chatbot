from functools import wraps
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from user.models import Profile

def authorize(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        request = args[1]
        auth = JWTAuthentication()
        try:
            header = auth.get_header(request)
            raw_token = auth.get_raw_token(header)
            validated_token = auth.get_validated_token(raw_token)
            request.user = auth.get_user(validated_token)
            try:
                request.user.profile = request.user.profile
            except Profile.DoesNotExist:
                return JsonResponse({'detail': 'User profile not found'}, status=404)

        except InvalidToken:
            return JsonResponse({'detail': 'Token is invalid or expired'}, status=403)
        except TokenError:
            return JsonResponse({'detail': 'Bad Token'}, status=400)
        return f(*args, **kwargs)
    return wrapper