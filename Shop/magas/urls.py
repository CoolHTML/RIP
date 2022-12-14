from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('api/token/obtain', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user', user, name='user'),
    path('', mainpage,name = 'main'),
    path('form/',RegisterUser.as_view(),name = 'registration'),
    path('login/',AuthUser.as_view(),name = 'login'),
    path('logout/', logout_user, name='logout'),
    path('ellizium/mainpage',ellizium_mainpage_view,name='ellizium_mainpage'),
    path('ellizium/rools',ellizium_rools_view,name='ellizium_rools'),
    path('findgame/',find_game_view,name = 'find_game'),
    path('profile/', profile, name='users-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('all_games/',view_all_games,name='all_games'),
    path('all_games/<int:id>',view_current_game,name='current_game'),
    path('profile/<int:id>',view_game,name='game_number'),
    path('deletegame/<str:player>/<int:id>',delete_page,name='delete_page'),
    path('addme/<str:player>/<int:id>',add_view,name='add_page'),
    path('profile/approved_games',approved_games,name ='approved_games'),
    path('send_json',getJson,name='getJson'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
