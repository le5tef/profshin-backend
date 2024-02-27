from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product import views

router = routers.DefaultRouter()

router.register(r'products', views.CatalogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include(router.urls))
    ])),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken'))
]
