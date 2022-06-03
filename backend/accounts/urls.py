from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
    
    path("suggestions/", views.SuggestionListAPIView.as_view(), name="suggestion_user_list"),
    
    path('follow/', views.user_follow, name='user_follow'),
    path('unfollow/', views.user_unfollow, name='user_unfollow'),
]

 