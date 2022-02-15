from django.urls import path
from rest_framework.routers import SimpleRouter  # new

from .views import PostViewSet, UserViewSet  # new

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls
