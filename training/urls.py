"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from myapp import urls as u
from rest_framework import routers
from myapp import views
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.authtoken.views import ObtainAuthToken


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'trainer', views.TrainerViewSet)
router.register(r'fetch', views.FetchUserViewSet)
router.register(r'info', views.trainerName)
router.register(r'email', views.EmailViewSet)
# router.register(r'token', views.sendToken)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i/', views.email,name = "efdg"),
    path('token/',views.verifyRegister.as_view()),
    # path('g/',views.sendToken,name="edf"),
    # path('api/', include('u')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path(r'api-token-auth/', obtain_jwt_token),
    # path(r'api-token-refresh/', refresh_jwt_token),
    path(r'auth/', ObtainAuthToken.as_view()),
    path('logout/', views.Logout.as_view()),
    # path(r'^activate/(?P[0-9A-Za-z_\-]+)/(?P[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/account/$',
    #     views.activate_user_account, name='activate_user_account'),
    # # path('app/', views.email, namespace='app')
    path('tt', views.test, name="efdg")
]