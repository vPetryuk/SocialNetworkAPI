from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import UserViewset, UserCreate, BlacklistTokenUpdateView

router = DefaultRouter()
router.register('user', UserViewset, basename='user')
from .views import apifunction, UserViewset , user_detail , UserGCList, UserGCDetail



urlpatterns = [
    path('create/', UserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist'),
    # path('viewset/', include(router.urls)),
    # path('funcapiuser/', apifunction),
    # path('funcapiuser/<int:pk>', user_detail ),
    path('GCuser/', UserGCList.as_view() ),

    path('GCuser/<int:pk>', UserGCDetail.as_view()),
]
