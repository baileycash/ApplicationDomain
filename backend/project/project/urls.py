from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
# from rest_framework.views import ObtainAuthToken
from users.views import UserViewSet, GroupViewSet

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(router.urls)),
    # path(r'api/token/', obtain_jwt_token),
    # path(r'api/token/refresh/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# urlpatterns += [
#     re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
# ]
#django no longer handles 404 errors; frontend does ^
