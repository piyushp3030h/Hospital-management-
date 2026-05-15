"""
URL configuration for PatientPro project.
"""

from django.contrib import admin
from django.urls import path, include

# JWT imports
from rest_framework_simplejwt.views import ( # pyright: ignore[reportMissingImports]
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Allauth
    path('accounts/', include('allauth.urls')),

    # Normal Django URLs
    path('', include('MediAccess.urls')),

    # DRF API URLs
    path('api/', include('MediAccess.api.urls')),

    # JWT Authentication APIs
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]