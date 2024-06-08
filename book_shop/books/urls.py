from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, AuthorViewSet, GenreViewSet ,LoginViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'users',LoginViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
