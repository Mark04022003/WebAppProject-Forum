from django.urls import path
from .views import signup, signin, update_profile, logout, activate

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("update_profile/", update_profile, name="update_profile"),
    path("logout/", logout, name="logout"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]