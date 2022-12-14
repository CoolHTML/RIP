"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from magas import views as games_views  #оно работает ошибки нет, пайчарм головой стукнулся
from django.urls import include, path
from rest_framework import routers
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'games', games_views.MyViewSet)
router.register(r'name', games_views.gamenViewset)
router.register(r'user', games_views.userViewset)
# models_router=routers.NestedDefaultRouter(router, r'games', lookup='games')
# models_router.register(r'models', games_views.ModelsOfTypeViewSet, basename='models-of-type')
router.register(r'bag', games_views.BagViewSet, basename='bag')
router.register(r'players_in_game', games_views.PlayersInGameViewSet, basename='players_in_game')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('auth/', include('rest_framework.urls')),
    path('',include('magas.urls')),
    path('', include(router.urls))
]
