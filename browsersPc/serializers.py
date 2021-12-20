from rest_framework import serializers

from browsersPc.models import Browsers, PC


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = "__all__"


class BrowsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Browsers
        fields = "__all__"
