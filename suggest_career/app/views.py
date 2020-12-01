import requests, json
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from rest_framework.permissions import BasePermission

from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from suggest_career.app.models import User, MBTI, TestHistory
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

# ___________________________________________________________________________
# ________________________흥미 검사____________________________________________
# ___________________________________________________________________________

class MiddleInterestTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        apiKey = '403f9bbdb00069287e869a9b302b406b'
        URL = 'http://inspct.career.go.kr/openapi/test/questions?apikey=' + apiKey + '&q=4'
        res = requests.get(URL)

        return HttpResponse(res, content_type='application/json')


class MiddleInterestAnswerViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        answer = request.data

        apikey = "403f9bbdb00069287e869a9b302b406b"

        answer_dict = {
            "apikey": apikey,
            "qestrnSeq": "4",
            "trgetSe": "100206",
            "name": user.username,
            "gender": "100323",
            "school": "중학교",
            "grade": "2",
            "email": "",
            "startDtm": 1550466291034,
            "answers": answer['answer']
        }

        url = 'http://inspct.career.go.kr/openapi/test/report?apikey=' + apikey + '&qestrnSeq=4'
        api_res_url = requests.post(url=url, json=answer_dict).json()['RESULT']['url']
        api_res_dict = {
            'url': api_res_url
        }
        api_res = json.dumps(api_res_dict, ensure_ascii=False)

        test_history = TestHistory()
        test_history.user = user
        test_history.result = api_res_url
        test_history.save()

        return HttpResponse(api_res, content_type='application/json')


# ___________________________________________________________________________

class HighInterestTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        apiKey = '403f9bbdb00069287e869a9b302b406b'
        URL = 'http://inspct.career.go.kr/openapi/test/questions?apikey=' + apiKey + '&q=5'
        res = requests.get(URL)

        return HttpResponse(res, content_type='application/json')


class HighInterestAnswerViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        answer = request.data

        apikey = "403f9bbdb00069287e869a9b302b406b"

        answer_dict = {
            "apikey": apikey,
            "qestrnSeq": "5",
            "trgetSe": "100207",
            "name": user.username,
            "gender": "100323",
            "school": "고등학교",
            "grade": "2",
            "email": "",
            "startDtm": 1550466291034,
            "answers": answer['answer']
        }

        url = 'http://inspct.career.go.kr/openapi/test/report?apikey=' + apikey + '&qestrnSeq=5'
        api_res_url = requests.post(url=url, json=answer_dict).json()['RESULT']['url']
        api_res_dict = {
            'url': api_res_url
        }
        api_res = json.dumps(api_res_dict, ensure_ascii=False)

        test_history = TestHistory()
        test_history.user = user
        test_history.result = api_res_url
        test_history.save()

        return HttpResponse(api_res, content_type='application/json')


# ___________________________________________________________________________
# ________________________적성 검사____________________________________________
# ___________________________________________________________________________

class MiddleAptitudeTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        apiKey = '403f9bbdb00069287e869a9b302b406b'
        URL = 'http://inspct.career.go.kr/openapi/test/questions?apikey=' + apiKey + '&q=20'
        res = requests.get(URL)

        return HttpResponse(res, content_type='application/json')


class MiddleAptitudeAnswerViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        answer = request.data

        apikey = "403f9bbdb00069287e869a9b302b406b"

        answer_dict = {
            "apikey": apikey,
            "qestrnSeq": "20",
            "trgetSe": "100206",
            "name": user.username,
            "gender": "100323",
            "school": "중학교",
            "grade": "2",
            "email": "",
            "startDtm": 1550466291034,
            "answers": answer['answer']
        }

        url = 'http://inspct.career.go.kr/openapi/test/report?apikey=' + apikey + '&qestrnSeq=20'
        api_res_url = requests.post(url=url, json=answer_dict).json()['RESULT']['url']
        api_res_dict = {
            'url': api_res_url
        }
        api_res = json.dumps(api_res_dict, ensure_ascii=False)

        test_history = TestHistory()
        test_history.user = user
        test_history.result = api_res_url
        test_history.save()

        return HttpResponse(api_res, content_type='application/json')


# ___________________________________________________________________________

class HighAptitudeTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        apiKey = '403f9bbdb00069287e869a9b302b406b'
        URL = 'http://inspct.career.go.kr/openapi/test/questions?apikey=' + apiKey + '&q=21'
        res = requests.get(URL)

        return HttpResponse(res, content_type='application/json')


class HighAptitudeAnswerViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        answer = request.data

        apikey = "403f9bbdb00069287e869a9b302b406b"

        answer_dict = {
            "apikey": apikey,
            "qestrnSeq": "21",
            "trgetSe": "100207",
            "name": user.username,
            "gender": "100323",
            "school": "고등학교",
            "grade": "2",
            "email": "",
            "startDtm": 1550466291034,
            "answers": answer['answer']
        }

        url = 'http://inspct.career.go.kr/openapi/test/report?apikey=' + apikey + '&qestrnSeq=21'
        api_res_url = requests.post(url=url, json=answer_dict).json()['RESULT']['url']
        api_res_dict = {
            'url': api_res_url
        }
        api_res = json.dumps(api_res_dict, ensure_ascii=False)

        test_history = TestHistory()
        test_history.user = user
        test_history.result = api_res_url
        test_history.save()

        return HttpResponse(api_res, content_type='application/json')


# ----------------------------------------------------------
# ----------------직업가치관 검사-------------------------------
# ----------------------------------------------------------

class ValueTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        apiKey = '403f9bbdb00069287e869a9b302b406b'
        URL = 'http://inspct.career.go.kr/openapi/test/questions?apikey=' + apiKey + '&q=6'
        res = requests.get(URL)

        return HttpResponse(res, content_type='application/json')


class ValueAnswerViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        answer = request.data

        apikey = "403f9bbdb00069287e869a9b302b406b"

        answer_dict = {
            "apikey": apikey,
            "qestrnSeq": "6",
            "trgetSe": "100206",
            "name": user.username,
            "gender": "100323",
            "school": "",
            "grade": "2",
            "email": "",
            "startDtm": 1550466291034,
            "answers": answer['answer']
        }

        url = 'http://inspct.career.go.kr/openapi/test/report?apikey=' + apikey + '&qestrnSeq=6'
        api_res_url = requests.post(url=url, json=answer_dict).json()['RESULT']['url']
        api_res_dict = {
            'url': api_res_url
        }
        api_res = json.dumps(api_res_dict, ensure_ascii=False)

        test_history = TestHistory()
        test_history.user = user
        test_history.result = api_res_url
        test_history.save()

        return HttpResponse(api_res, content_type='application/json')


# ----------------------------------------------------------
# ----------------이공계전공적합도-------------------------------
# ----------------------------------------------------------

class SEAptitudeTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        apiKey = '403f9bbdb00069287e869a9b302b406b'
        URL = 'http://inspct.career.go.kr/openapi/test/questions?apikey=' + apiKey + '&q=9'
        res = requests.get(URL)

        return HttpResponse(res, content_type='application/json')


class SEAptitudeAnswerViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        answer = request.data

        apikey = "403f9bbdb00069287e869a9b302b406b"

        answer_dict = {
            "apikey": apikey,
            "qestrnSeq": "9",
            "trgetSe": "100206",
            "name": user.username,
            "gender": "100323",
            "school": "",
            "grade": "2",
            "email": "",
            "startDtm": 1550466291034,
            "answers": answer['answer']
        }

        url = 'http://inspct.career.go.kr/openapi/test/report?apikey=' + apikey + '&qestrnSeq=9'
        api_res_url = requests.post(url=url, json=answer_dict).json()['RESULT']['url']
        api_res_dict = {
            'url': api_res_url
        }
        api_res = json.dumps(api_res_dict, ensure_ascii=False)

        test_history = TestHistory()
        test_history.user = user
        test_history.result = api_res_url
        test_history.save()

        return HttpResponse(api_res, content_type='application/json')


# ----------------------------------------------------------
# ----------------유저 히스토리--------------------------------
# ----------------------------------------------------------

class UserHistoryViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        test_history_list = user.history_user.all()

        test_history_url_list = []
        for i in range(len(test_history_list)):
            test_history_url_list.append(test_history_list[i].result)

        dict = {
            'answer': test_history_url_list
        }

        resJson = json.dumps(dict, ensure_ascii=False)
        return HttpResponse(resJson, content_type='application/json')


# ----------------------------------------------------------
# ----------------MBTI--------------------------------------
# ----------------------------------------------------------

class MBTISaveViewSet(APIView):
    def post(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        mbti = request.data['mbti']

        user.mbti = mbti
        u = user.save()

        return JsonResponse({
            "detail": "MBTI saved"
        })


class MBTIViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)
        mbti = MBTI.objects.get(type=user.mbti)

        res_dict = {
            "job": mbti.list
        }
        resJson = json.dumps(res_dict, ensure_ascii=False)
        return HttpResponse(resJson, content_type='application/json')


class UnivAptitudeTestViewSet(APIView):
    def get(self, request, user_pk, *args, **kwargs):
        user = User.objects.get(id=user_pk)