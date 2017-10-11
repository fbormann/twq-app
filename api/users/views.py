from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer


class UserView(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None, **kwargs):
        if kwargs.get('user_id'):
            try:
                user = User.objects.get(id=kwargs['user_id'])
                user_data = UserSerializer(user)
                return Response(user_data.data)
            except ObjectDoesNotExist:
                return Response({"error": "could not find user"}    , status=400)
        else:
            all_users = User.objects.all()
            all_users_serialized = UserSerializer(all_users, many=True)
            return Response(all_users_serialized.data)

    def post(self, request, format=None):
        response = Response()
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            response.status_code = 201
        else:
            response.status_code = 400
        return response

    def delete(self, request, format=None, **kwargs):
        response = Response()
        if kwargs.get("user_id"):
            user = User.objects.get(id=kwargs['user_id'])
            if user:
                user.delete()
                response.status_code = 204
            else:
                pass
        else:
            response.status_code = 400

        return response