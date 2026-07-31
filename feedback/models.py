from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def feedback_photo_path(instance, filename):
    return f"feedback_photos/{filename}"


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    message = models.TextField(max_length=500)
    photo = models.ImageField(
        upload_to=feedback_photo_path, blank=True, null=True
    )
    route = models.CharField(max_length=150, blank=True)
    is_approved = models.BooleanField(default=True)
    likes = models.PositiveIntegerField(default=0)
    laugh_count = models.PositiveIntegerField(default=0)
    wow_count = models.PositiveIntegerField(default=0)
    clap_count = models.PositiveIntegerField(default=0)
    admin_reply = models.TextField(max_length=500, blank=True)
    admin_reply_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.rating}★) - {'approved' if self.is_approved else 'pending'}"


class FeedbackComment(models.Model):
    feedback = models.ForeignKey(Feedback, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.name} on feedback #{self.feedback_id}"
