from rest_framework.routers import DefaultRouter
from calibration_api.views import UserViewSet

router = DefaultRouter()
#TODO: change this line
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls
