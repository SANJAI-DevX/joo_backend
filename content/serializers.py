from rest_framework import serializers

from .models import ContactInfo, ContentBlock, Driver


class ContentBlockPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ["key", "value_en", "value_ta"]


class ContentBlockAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ["id", "section", "key", "label", "value_en", "value_ta", "order", "updated_at"]
        read_only_fields = ["id", "section", "key", "label", "order", "updated_at"]


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ["id", "name", "phone", "order"]
        read_only_fields = ["id"]


class ContactInfoSerializer(serializers.ModelSerializer):
    drivers = DriverSerializer(many=True, read_only=True)

    class Meta:
        model = ContactInfo
        fields = [
            "whatsapp_number",
            "drivers",
            "email",
            "address",
            "updated_at",
        ]
        read_only_fields = ["updated_at"]
