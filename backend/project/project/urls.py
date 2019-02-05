from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from users import views

from pages.views import FrontendRenderView

router = routers.DefaultRouter()
# router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('users.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# urlpatterns += [
#     re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
# ]
#django no longer handles 404 errors; frontend does ^
