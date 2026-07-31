from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from .models import Feedback, FeedbackComment


class FeedbackCommentInline(admin.TabularInline):
    model = FeedbackComment
    extra = 0
    readonly_fields = ("name", "message", "created_at")
    can_delete = True


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "route", "likes", "is_approved", "created_at", "photo_thumb")
    list_filter = ("is_approved", "rating", "created_at")
    search_fields = ("name", "message", "route")
    readonly_fields = ("created_at", "reviewed_at", "photo_preview", "likes", "laugh_count", "wow_count", "clap_count", "admin_reply_at")
    actions = ("approve_feedback", "reject_feedback")
    inlines = [FeedbackCommentInline]
    fields = (
        "name",
        "rating",
        "message",
        "route",
        "photo",
        "photo_preview",
        "is_approved",
        "likes",
        "laugh_count",
        "wow_count",
        "clap_count",
        "admin_reply",
        "admin_reply_at",
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


@admin.register(FeedbackComment)
class FeedbackCommentAdmin(admin.ModelAdmin):
    list_display = ("name", "feedback", "message", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "message")
    readonly_fields = ("feedback", "name", "message", "created_at")
