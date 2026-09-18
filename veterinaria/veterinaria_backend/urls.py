from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # TokenAuthentication:
    # POST /api/token/ con username + password.
    path('api/token/', obtain_auth_token, name='api_token'),

    path('clinica/', include('clinica.urls')),
]
