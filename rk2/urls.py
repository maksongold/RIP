from rest_framework import routers
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from browsersPc import views as views

router = routers.DefaultRouter()
router.register('pc', views.PCViewSet)
router.register('browsers', views.BrowsersViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('report/', views.report),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]