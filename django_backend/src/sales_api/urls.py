from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import TestView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('rest-auth/', include('rest_auth.urls'))
]
