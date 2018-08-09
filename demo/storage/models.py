from django.db import models
from mongoengine import fields as mongo_fields
from mongoengine import EmbeddedDocument

class DataSet(models.Model):
    id = models.CharField(
        primary_key=True, db_index=True, unique=True,
        max_length=30)
    text = models.TextField()
    user_id = models.CharField(max_length=20)  # may be foreign key?
    user_name = models.CharField(max_length=20)
    time = models.DateTimeField()
    source = models.CharField(max_length=20)
    sentiment = models.CharField(max_length=20)  # may be choice field?
    senti_strings = models.CharField(max_length=20)  # may be choice field?
    labelled_sentiment = models.CharField(max_length=20)  # may be choice field?
    crowder = models.CharField(max_length=20)  # may be foreign key?
    coor_x = models.DecimalField(max_digits=20, decimal_places=10)
    coor_y = models.DecimalField(max_digits=20, decimal_places=10)

    @property
    def time_day(self):
        return self.time.day

    @property
    def time_month(self):
        return self.time.month

    @property
    def time_year(self):
        return self.time.year

    @property
    def time_hour(self):
        return self.time.hour

    @property
    def time_minute(self):
        return self.time.minute

    @property
    def time_second(self):
        return self.time.second


class UnstructuredDataSet(EmbeddedDocument):
    name = mongo_fields.StringField(required=True)
    value = mongo_fields.DynamicField(required=True)
