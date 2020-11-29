import requests
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission

from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from suggest_career.app.models import User
from suggest_career.app.serializer import UserInfoSerializer, SignInSerializer, SignUpSerializer


class UserViewSet(viewsets.ModelViewSet):
    class UserPermissionClass(BasePermission):
        def has_permission(self, request, view):
            return True

        def has_object_permission(self, request, view, obj):
            return request.user == obj

    @action(methods=['POST'], detail=False)
    def signin(self, request, *args, **kwargs):
        s = SignInSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        u = User.objects.get(username=request.data.get('username'))
        return Response(UserInfoSerializer(instance=u).data, status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def signup(self, request, *args, **kwargs):
        s = SignUpSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        u = s.save()
        return Response(UserInfoSerializer(instance=u).data, status.HTTP_201_CREATED)

    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.AllowAny]


class HighInterestTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        apiKey = '403f9bbdb00069287e869a9b302b406b'
        URL = 'http://inspct.career.go.kr/openapi/test/questions?apikey='+apiKey+'&q=5'
        res = requests.get(URL)

        return HttpResponse(res, content_type='application/json')


class HighInterestAnswerViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        dict = {

        }


class ValueTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)

class UnivAptitudeTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
