from rest_framework.serializers import ModelSerializer
from rest_framework_recursive.fields import RecursiveField
from .models import (
    Section,
    Item,
    Modifier,
)

class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

class ModifierSerializer(ModelSerializer):
    class Meta:
        model = Modifier
        fields = "__all__"

# Index Serializers

class IndexModifierSerializer(ModelSerializer):
    class Meta:
        model = Modifier
        fields = "__all__"

class IndexItemSerializer(ModelSerializer):
    modifiers = IndexModifierSerializer(read_only=True, many=True)
    class Meta:
        model = Item
        fields = "__all__"

class IndexSerializer(ModelSerializer):
    items = IndexItemSerializer(read_only=True, many=True)
    class Meta:
        model = Section
        fields = "__all__"