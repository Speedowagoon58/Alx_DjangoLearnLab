from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
["login/", "register/"]
["unfollow/<int:user_id>/", "follow/<int:user_id>"]