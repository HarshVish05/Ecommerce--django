from django.urls import path

from core.views.user_views import getUserProfile, getUsers, register_user, MyTokenObtainPairView

app_name = 'core'

urlpatterns = [
    path('', getUsers, name="allusers"),
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register_user, name="register"),
    path('profile/', getUserProfile, name="profile"),
]
