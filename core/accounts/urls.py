from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token),
]

from .views import ProtectedView, AdminOnlyView

urlpatterns += [
    path('me/', ProtectedView.as_view()),
    path('admin-only/', AdminOnlyView.as_view()),

]