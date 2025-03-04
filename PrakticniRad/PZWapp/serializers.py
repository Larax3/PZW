from rest_framework import serializers
from .models import PovrtnaBiljka, VrtnaBiljka

class PovrtnaBiljkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PovrtnaBiljka
        fields = '__all__'

class VrtnaBiljkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VrtnaBiljka
        fields = '__all__'