from django.conf.urls import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_nested import routers

from suggest_career.app import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

user_router = routers.NestedDefaultRouter(router, r'users', lookup='user')

# user_router.register(r'quiz/false', views.QuizViewSet, basename='quiz')

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path(r'api/v1/', include(router.urls)),
    path(r'api/v1/', include(user_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ### 흥미검사
    url('api/v1/users/(?P<user_pk>[0-9]+)/question/high/interest', views.HighInterestTestViewSet.as_view()),
    url('api/v1/users/(?P<user_pk>[0-9]+)/answer/high/interest', views.HighInterestAnswerViewSet.as_view()),

    url('api/v1/users/(?P<user_pk>[0-9]+)/question/middle/interest', views.MiddleInterestTestViewSet.as_view()),
    url('api/v1/users/(?P<user_pk>[0-9]+)/answer/middle/interest', views.MiddleInterestAnswerViewSet.as_view()),

    ### 적성검사
    url('api/v1/users/(?P<user_pk>[0-9]+)/question/high/aptitude', views.HighAptitudeTestViewSet.as_view()),
    url('api/v1/users/(?P<user_pk>[0-9]+)/answer/high/aptitude', views.HighAptitudeAnswerViewSet.as_view()),

    url('api/v1/users/(?P<user_pk>[0-9]+)/question/middle/aptitude', views.MiddleAptitudeTestViewSet.as_view()),
    url('api/v1/users/(?P<user_pk>[0-9]+)/answer/middle/aptitude', views.MiddleAptitudeAnswerViewSet.as_view()),

    ### 직업 가치관 검사
    url('api/v1/users/(?P<user_pk>[0-9]+)/question/common/value', views.ValueTestViewSet.as_view()),
    url('api/v1/users/(?P<user_pk>[0-9]+)/answer/common/value', views.ValueAnswerViewSet.as_view()),

    ### 이공계적합도 검사
    url('api/v1/users/(?P<user_pk>[0-9]+)/question/common/se', views.SEAptitudeTestViewSet.as_view()),
    url('api/v1/users/(?P<user_pk>[0-9]+)/answer/common/se', views.SEAptitudeAnswerViewSet.as_view()),

    ### 테스트 히스토리 조회
    url('api/v1/users/(?P<user_pk>[0-9]+)/testhistory', views.UserHistoryViewSet.as_view()),

    ### MBTI
    url('api/v1/users/(?P<user_pk>[0-9]+)/mbti/save', views.MBTISaveViewSet.as_view()),
    url('api/v1/users/(?P<user_pk>[0-9]+)/mbti/view', views.MBTIViewSet.as_view()),

]

