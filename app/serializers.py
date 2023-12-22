from rest_framework import serializers
from .models import ConceptoGasto

class ConceptoGastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConceptoGasto
        fields = '__all__'