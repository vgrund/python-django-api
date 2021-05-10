from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics, views, status
from .serializers import UserSerializer
from .models import User
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.response import Response


class UserList(views.APIView):
    serializer_class = UserSerializer
    filter_fields = '__all__'

    @extend_schema(
        description='Get a list of all users',
        operation_id='get-all',
        tags=['Users'],
        responses={(status.HTTP_200_OK, 'application/json'): UserSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(data=User.objects.all(), many=True)
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        description='Create a user',
        operation_id='create',
        tags=['Users'],
        request={('application/json'): UserSerializer},
        responses={(status.HTTP_201_CREATED, 'application/json'): UserSerializer}
    )
    def post(self, request):
        User.objects.create(
            id=request.POST['id'],
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            email=request.POST['email'],
            phone=request.POST['phone'])
        return Response(request.data, status=status.HTTP_201_CREATED)


class UserDetail(views.APIView):
    serializer_class = UserSerializer
    filter_fields = '__all__'

    @extend_schema(
        description='Get a user by its id',
        operation_id='get-by-id',
        tags=['Users'],
        responses={(status.HTTP_200_OK, 'application/json'): UserSerializer}
    )
    def get(self, request, id, *args, **kwargs):
        serializer = UserSerializer(User.objects.select_related().get(pk=id))
        return Response(data=serializer.data, status=status.HTTP_200_OK)
