from rest_framework import serializers
from models import Allergies, Components


class AllergySerializer(serializers.ModelSerializer):

    class Meta:
        model = Allergies


class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Components
