from rest_framework import serializers

from .models import ContactInfo, ContentBlock


class ContentBlockPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ["key", "value_en", "value_ta"]


class ContentBlockAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ["id", "section", "key", "label", "value_en", "value_ta", "order", "updated_at"]
        read_only_fields = ["id", "section", "key", "label", "order", "updated_at"]


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = [
            "whatsapp_number",
            "driver1_name",
            "driver1_phone",
            "driver2_name",
            "driver2_phone",
            "email",
            "address",
            "updated_at",
        ]
        read_only_fields = ["updated_at"]
