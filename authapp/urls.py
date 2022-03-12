
from django.urls import path, include
from . import views
urlpatterns = [

    path('', include('User.urls')),

]

