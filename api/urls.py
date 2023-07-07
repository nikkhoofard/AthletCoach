from django.urls import path, include
from . import views
from .views import UserProfileViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("profile", UserProfileViewSet, basename='profile')
router.register("profile/create-action", UserProfileViewSet, basename='action')
urlpatterns = [
    path("", include(router.urls)),
    path(r"auth/", include('djoser.urls')),
    path(r'^auth/', include('djoser.urls.authtoken')),

    #path("users/int:<pk>", UserDetail.as_view())
    #path('api/instances/', views.InstanceList.as_view(), name="instances"),

]
