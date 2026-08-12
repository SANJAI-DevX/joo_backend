from django.contrib import admin

from .models import ContactInfo, ContentBlock, Driver


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ("key", "section", "label", "updated_at")
    list_filter = ("section",)
    search_fields = ("key", "label", "value_en", "value_ta")
    fields = ("section", "key", "label", "value_en", "value_ta", "order")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "order")
    ordering = ("order", "id")
