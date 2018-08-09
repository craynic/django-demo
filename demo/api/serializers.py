import datetime
from rest_framework import serializers

from storage.models import DataSet


class DataSetSerializer(serializers.ModelSerializer):
    userID = serializers.CharField(source='user_id', max_length=20)
    userName = serializers.CharField(source='user_name', max_length=20)
    day = serializers.IntegerField(source='time_day')
    month = serializers.IntegerField(source='time_month')
    year = serializers.IntegerField(source='time_year')
    hour = serializers.IntegerField(source='time_hour')
    minute = serializers.IntegerField(source='time_minute')
    second = serializers.IntegerField(source='time_second')
    sentiStrings = serializers.CharField(source='senti_strings', max_length=20)
    labelledSentiment = serializers.CharField(
        source='labelled_sentiment', max_length=20)

    def validate(self, data):
        print(data)
        data['time'] = datetime.datetime(
            data['time_year'], data['time_month'], data['time_day'],
            data['time_hour'], data['time_minute'], data['time_second'])
        del data['time_year']
        del data['time_month']
        del data['time_day']
        del data['time_hour']
        del data['time_minute']
        del data['time_second']
        return data

    class Meta:
        model = DataSet
        fields = (
            'id', 'text', 'userID', 'userName',
            'day', 'month', 'year', 'hour', 'minute', 'second',
            'source', 'sentiment', 'sentiStrings', 'labelledSentiment',
            'crowder', 'coor_x', 'coor_y')
