from django.conf import settings
from django.utils import timezone
from rest_framework import serializers

from .models import Feedback, FeedbackComment

ALLOWED_PHOTO_TYPES = ("image/jpeg", "image/png", "image/webp")


class FeedbackListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    reactions = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = [
            "id",
            "name",
            "rating",
            "message",
            "route",
            "photo",
            "reactions",
            "comment_count",
            "admin_reply",
            "admin_reply_at",
            "created_at",
        ]

    def get_photo(self, obj):
        if not obj.photo:
            return None
        request = self.context.get("request")
        url = obj.photo.url
        return request.build_absolute_uri(url) if request else url

    def get_reactions(self, obj):
        return {
            "love": obj.likes,
            "laugh": obj.laugh_count,
            "wow": obj.wow_count,
            "clap": obj.clap_count,
        }

    def get_comment_count(self, obj):
        # Uses the annotated count from the queryset when available (avoids
        # one extra query per row); falls back to a live count only if this
        # serializer is ever used with a queryset that wasn't annotated.
        annotated = getattr(obj, "comment_count_annotated", None)
        return annotated if annotated is not None else obj.comments.count()


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["name", "rating", "message", "route", "photo"]

    def validate_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Please enter your full name.")
        return value

    def validate_message(self, value):
        value = value.strip()
        if len(value) < 5:
            raise serializers.ValidationError("Please share a little more detail in your feedback.")
        return value

    def validate_photo(self, value):
        if value is None:
            return value
        if value.content_type not in ALLOWED_PHOTO_TYPES:
            raise serializers.ValidationError("Photo must be a JPEG, PNG, or WEBP image.")
        max_size_mb = getattr(settings, "FEEDBACK_MAX_PHOTO_SIZE_MB", 5)
        if value.size > max_size_mb * 1024 * 1024:
            raise serializers.ValidationError(f"Photo must be smaller than {max_size_mb}MB.")
        return value


class FeedbackAdminSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField(read_only=True)
    photo_upload = serializers.ImageField(source="photo", write_only=True, required=False, allow_null=True)
    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = [
            "id",
            "name",
            "rating",
            "message",
            "route",
            "photo",
            "photo_upload",
            "is_approved",
            "reactions",
            "admin_reply",
            "admin_reply_at",
            "created_at",
            "reviewed_at",
        ]
        read_only_fields = ["id", "reactions", "admin_reply_at", "created_at", "reviewed_at"]

    def get_photo(self, obj):
        if not obj.photo:
            return None
        request = self.context.get("request")
        url = obj.photo.url
        return request.build_absolute_uri(url) if request else url

    def get_reactions(self, obj):
        return {
            "love": obj.likes,
            "laugh": obj.laugh_count,
            "wow": obj.wow_count,
            "clap": obj.clap_count,
        }

    def validate_photo_upload(self, value):
        if value is None:
            return value
        if value.content_type not in ALLOWED_PHOTO_TYPES:
            raise serializers.ValidationError("Photo must be a JPEG, PNG, or WEBP image.")
        max_size_mb = getattr(settings, "FEEDBACK_MAX_PHOTO_SIZE_MB", 5)
        if value.size > max_size_mb * 1024 * 1024:
            raise serializers.ValidationError(f"Photo must be smaller than {max_size_mb}MB.")
        return value

    def update(self, instance, validated_data):
        was_approved = instance.is_approved
        old_reply = instance.admin_reply
        instance = super().update(instance, validated_data)

        update_fields = []
        if "is_approved" in validated_data and validated_data["is_approved"] != was_approved:
            instance.reviewed_at = timezone.now()
            update_fields.append("reviewed_at")
        if "admin_reply" in validated_data and validated_data["admin_reply"] != old_reply:
            instance.admin_reply_at = timezone.now() if validated_data["admin_reply"] else None
            update_fields.append("admin_reply_at")
        if update_fields:
            instance.save(update_fields=update_fields)
        return instance


class FeedbackCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackComment
        fields = ["id", "name", "message", "created_at"]


class FeedbackCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackComment
        fields = ["name", "message"]

    def validate_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError("Please enter your name.")
        return value

    def validate_message(self, value):
        value = value.strip()
        if len(value) < 1:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value
