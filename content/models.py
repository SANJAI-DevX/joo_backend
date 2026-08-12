from django.db import models


class ContentBlock(models.Model):
    HOME = "home"
    CONTACT = "contact"
    FOOTER = "footer"

    SECTION_CHOICES = [
        (HOME, "Home Page"),
        (CONTACT, "Contact"),
        (FOOTER, "About / Footer"),
    ]

    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    key = models.SlugField(max_length=60, unique=True)
    label = models.CharField(max_length=150)
    value_en = models.TextField()
    value_ta = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["section", "order", "id"]

    def __str__(self):
        return f"[{self.section}] {self.key}"


class ContactInfo(models.Model):
    """Singleton row holding the site's live contact/WhatsApp numbers."""

    whatsapp_number = models.CharField(
        max_length=20, help_text="Digits only with country code, e.g. 919524788173"
    )
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1, defaults={"whatsapp_number": "919524788173"})
        return obj

    def __str__(self):
        return "Contact Info"


class Driver(models.Model):
    """One driver entry shown on the public site (footer) and editable as a list in admin."""

    contact_info = models.ForeignKey(ContactInfo, related_name="drivers", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.name} ({self.phone})"
