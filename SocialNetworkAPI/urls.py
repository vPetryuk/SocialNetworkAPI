
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
    path('user/', include('User.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('authapp.urls')),
]

