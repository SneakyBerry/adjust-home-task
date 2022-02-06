from rest_framework import serializers

from adjust.models import Adjust


class AdjustSerializer(serializers.ModelSerializer):
    cpi = serializers.FloatField(read_only=True)
    date = serializers.DateField(required=False)
    channel = serializers.CharField(required=False)
    spend = serializers.FloatField(required=False)
    revenue = serializers.FloatField(required=False)
    country = serializers.CharField(required=False)
    os = serializers.CharField(required=False)

    class Meta:
        model = Adjust
        fields = "__all__"
