from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from calibration_api.models.user import User
from calibration_api.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ViewSet):
    """
    A ViewSet for managing User CRUD operations.
    """

    @action(methods=['GET'], detail=False, url_path='')
    def get_users(self, request):
        """
        Retrieve all users.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"message": "success", "data": serializer.data, "error": None}, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True, url_path='details')
    def get_user(self, request, pk=None):
        """
        Retrieve a single user by ID.
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response({"message": "success", "data": serializer.data, "error": None}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "error", "data": None, "error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['POST'], detail=False, url_path='create')
    def add_user(self, request):
        """
        Create a new user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success", "data": serializer.data, "error": None}, status=status.HTTP_201_CREATED)
        return Response({"message": "error", "data": None, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['PUT'], detail=True, url_path='update')
    def update_user(self, request, pk=None):
        """
        Update an existing user by ID.
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "success", "data": serializer.data, "error": None}, status=status.HTTP_200_OK)
            return Response({"message": "error", "data": None, "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "error", "data": None, "error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['DELETE'], detail=True, url_path='delete')
    def delete_user(self, request, pk=None):
        """
        Delete a user by ID.
        """
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({"message": "success", "data": None, "error": None}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"message": "error", "data": None, "error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
