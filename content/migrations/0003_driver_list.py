import django.db.models.deletion
from django.db import migrations, models

LEGACY_DRIVER_COLUMNS = ("driver1_name", "driver1_phone", "driver2_name", "driver2_phone")


def _existing_columns(schema_editor, table_name):
    connection = schema_editor.connection
    with connection.cursor() as cursor:
        return {col.name for col in connection.introspection.get_table_description(cursor, table_name)}


def migrate_existing_drivers_forward(apps, schema_editor):
    """Carry any existing driver1/driver2 values over to the new Driver model,
    then drop the legacy columns.

    Written defensively: some databases may already be missing one or more of
    these columns (e.g. after a manual reset), in which case we skip whatever
    isn't there instead of erroring out.
    """
    ContactInfo = apps.get_model("content", "ContactInfo")
    Driver = apps.get_model("content", "Driver")

    table_name = ContactInfo._meta.db_table
    existing_columns = _existing_columns(schema_editor, table_name)

    # Only touch the ORM row if every legacy column is present -- a SELECT
    # against the historical model asks for all of them at once, so if even
    # one is missing the whole query fails.
    if set(LEGACY_DRIVER_COLUMNS).issubset(existing_columns):
        info = ContactInfo.objects.filter(pk=1).first()
        if info:
            order = 0
            if info.driver1_name or info.driver1_phone:
                Driver.objects.create(
                    contact_info=info,
                    name=info.driver1_name,
                    phone=info.driver1_phone,
                    order=order,
                )
                order += 1
            if info.driver2_name or info.driver2_phone:
                Driver.objects.create(
                    contact_info=info,
                    name=info.driver2_name,
                    phone=info.driver2_phone,
                    order=order,
                )

    # Drop whichever legacy columns are actually present. Columns already
    # absent are left alone rather than raising.
    for field_name in LEGACY_DRIVER_COLUMNS:
        if field_name in existing_columns:
            field = ContactInfo._meta.get_field(field_name)
            schema_editor.remove_field(ContactInfo, field)


def migrate_existing_drivers_backward(apps, schema_editor):
    # No-op: this migration is not designed to be reversed automatically.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0002_seed_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=60)),
                ("phone", models.CharField(max_length=20)),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "contact_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="drivers",
                        to="content.contactinfo",
                    ),
                ),
            ],
            options={
                "ordering": ["order", "id"],
            },
        ),
        migrations.RunPython(migrate_existing_drivers_forward, migrate_existing_drivers_backward),
        # The column drops themselves already happened (conditionally) inside
        # the RunPython above via schema_editor.remove_field. These entries
        # only update Django's model state so later migrations agree the
        # fields are gone -- they don't touch the database again.
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(model_name="contactinfo", name="driver1_name"),
                migrations.RemoveField(model_name="contactinfo", name="driver1_phone"),
                migrations.RemoveField(model_name="contactinfo", name="driver2_name"),
                migrations.RemoveField(model_name="contactinfo", name="driver2_phone"),
            ],
            database_operations=[],
        ),
    ]
