from django.urls import path, include

from .views import GoogleLogin, google_callback_handler, GitHubLogin, github_callback_handler

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
        
    path('google/login/', GoogleLogin.as_view(), name='google_login'),
    path('google/login/callback/', google_callback_handler, name='google_callback'),

    path('github/login/', GitHubLogin.as_view(), name='github_login'),
    path('github/login/callback/', github_callback_handler, name='github_callback'),
]