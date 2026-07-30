import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContentBlock",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "section",
                    models.CharField(
                        choices=[("home", "Home Page"), ("contact", "Contact"), ("footer", "About / Footer")],
                        max_length=20,
                    ),
                ),
                ("key", models.SlugField(max_length=60, unique=True)),
                ("label", models.CharField(max_length=150)),
                ("value_en", models.TextField()),
                ("value_ta", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["section", "order", "id"],
            },
        ),
        migrations.CreateModel(
            name="ContactInfo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "whatsapp_number",
                    models.CharField(
                        help_text="Digits only with country code, e.g. 919524788173", max_length=20
                    ),
                ),
                ("driver1_name", models.CharField(blank=True, max_length=60)),
                ("driver1_phone", models.CharField(blank=True, max_length=20)),
                ("driver2_name", models.CharField(blank=True, max_length=60)),
                ("driver2_phone", models.CharField(blank=True, max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("address", models.CharField(blank=True, max_length=255)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Contact Info",
                "verbose_name_plural": "Contact Info",
            },
        ),
    ]
