from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from application_user.views import ApplicationUserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('application_user.urls')),
    path('api/bugs/', include('tracker.urls')),
    path('api/token/', ApplicationUserLoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]
