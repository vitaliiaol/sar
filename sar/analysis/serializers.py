from rest_framework import serializers
from .models import Allergies, Analysis, Components


class AllergySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Allergies
        fields = ['id', 'algname', 'description']


class ComponentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    allergies = AllergySerializer(many=True)

    class Meta:
        model = Components
        fields = ['id', 'compname', 'description', 'firsthalf', 'secondhalf', 'allergies']


class AnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analysis
        fields = '__all__'


class AnalysisPostSerializer(serializers.Serializer):

    components = ComponentSerializer(many=True)

    class Meta:
        fields = ['components']