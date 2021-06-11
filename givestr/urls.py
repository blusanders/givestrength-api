from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from givestrapi.models import *
from givestrapi.views import *

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
]