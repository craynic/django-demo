from rest_framework import routers
from api.views import DataSetViewSet


router = routers.DefaultRouter()
router.register(r'dataset', DataSetViewSet)

urlpatterns = router.urls
