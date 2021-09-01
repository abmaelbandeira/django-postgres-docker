from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'description', 'price')
