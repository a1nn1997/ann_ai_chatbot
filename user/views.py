from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import UserSerializer, PasswordChangeSerializer, ProfileSerializer
from chatbot_app.decorators import authorize 
from user.models import Profile

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Create JWT tokens for the new user
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED, headers=headers)

    @authorize
    def change_password(self, request):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @authorize
    def list(self, request, *args, **kwargs):
        # List all user profiles
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    @authorize
    def retrieve(self, request, pk=None, *args, **kwargs):
        # Retrieve a specific user's profile
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    @authorize
    def partial_update(self, request, pk=None, *args, **kwargs):
        # Update a specific user's profile
        profile = request.user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

