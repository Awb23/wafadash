"""
URL configuration for wafadash project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Your App's API routes
    path('api/', include('USERS.urls')),
    
    # JWT Authentication routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # This catch-all route MUST be last. It serves the React app.
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),
]