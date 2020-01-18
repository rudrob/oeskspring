from django.urls import include, path
from rest_framework import routers
from oeskspring.oeskspring import views
from django.conf.urls import url
from django.contrib import admin
from rest_framework.authtoken import views as auth_views


router = routers.DefaultRouter()
# router.register(r'measurements', views.AllMeasurementsView)
urlpatterns = router.urls

urlpatterns = [
    # path('', include('shopcmsbackend.urls')),
    url(r'^api-token-auth/', auth_views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'^measurements/', views.AllMeasurementsView.as_view()),
    url(r'^upload', views.FileUploadView.as_view()),
    url(r'^router/', include(router.urls))
    ]