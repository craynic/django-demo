from rest_framework import routers
from api.views import DataSetViewSet, UnstructuredDataSetViewSet


router = routers.DefaultRouter()
router.register(r'dataset', DataSetViewSet)
router.register(r'unstructured', UnstructuredDataSetViewSet,
                base_name='unstructured')

urlpatterns = router.urls
