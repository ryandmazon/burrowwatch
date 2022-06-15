from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt import views as jwt_views

from server.users.register import RegisterApi
from server.users.api.views import UserViewSet
from server.users.auth_token import MyTokenObtainPairView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path('login', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('register', RegisterApi.as_view(), name='register'),
]


app_name = "api"
urlpatterns = router.urls
