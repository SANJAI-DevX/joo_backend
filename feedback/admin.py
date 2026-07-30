from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "route", "is_approved", "created_at", "photo_thumb")
    list_filter = ("is_approved", "rating", "created_at")
    search_fields = ("name", "message", "route")
    readonly_fields = ("created_at", "reviewed_at", "photo_preview")
    actions = ("approve_feedback", "reject_feedback")
    fields = (
        "name",
        "rating",
        "message",
        "route",
        "photo",
        "photo_preview",
        "is_approved",
        "created_at",
        "reviewed_at",
    )

    def photo_thumb(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height:40px;border-radius:50%;" />', obj.photo.url)
        return "—"

    photo_thumb.short_description = "Photo"

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height:200px;border-radius:8px;" />', obj.photo.url)
        return "No photo uploaded"

    photo_preview.short_description = "Preview"

    @admin.action(description="Approve selected feedback")
    def approve_feedback(self, request, queryset):
        updated = queryset.update(is_approved=True, reviewed_at=timezone.now())
        self.message_user(request, f"{updated} feedback item(s) approved.")

    @admin.action(description="Reject / hide selected feedback")
    def reject_feedback(self, request, queryset):
        updated = queryset.update(is_approved=False, reviewed_at=timezone.now())
        self.message_user(request, f"{updated} feedback item(s) rejected.")
