from rest_framework import routers

from .views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet
)

router = routers.DefaultRouter()
router.register('genres', GenreViewSet)
router.register('actors', ActorViewSet)
router.register('cinemahalls', CinemaHallViewSet)
router.register('movies', MovieViewSet)
router.register('moviesessions', MovieSessionViewSet)

urlpatterns = router.urls

app_name = 'cinema'
