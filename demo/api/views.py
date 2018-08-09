import bson.json_util
from django.conf import settings
import pymongo
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status, mixins, renderers

from storage.models import DataSet
from api.serializers import DataSetSerializer


class DataSetViewSet(
    mixins.ListModelMixin,
    GenericViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)


class MongoObjectRenderer(renderers.JSONRenderer):
    def render(self, data, media_type=None, renderer_context=None):
        serialized = bson.json_util.dumps(data)
        return bytes(serialized, 'utf-8')


class UnstructuredDataSetViewSet(GenericViewSet):
    renderer_classes = (MongoObjectRenderer,)

    def get_mongodb(self):
        client = pymongo.MongoClient()
        collection = client[settings.MONGODB_DATABASE][settings.MONGODB_COLLECTION]
        return collection

    def create(self, request):
        dbc = self.get_mongodb()
        dbc.insert_many(request.data)
        return Response(request.data)

    def list(self, request):
        dbc = self.get_mongodb()
        data = dbc.find()
        return Response(data)
