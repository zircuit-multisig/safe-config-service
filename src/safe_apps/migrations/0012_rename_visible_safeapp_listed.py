# Generated by Django 4.2.2 on 2024-05-08 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("safe_apps", "0011_alter_safeapp_icon_url"),
    ]

    operations = [
        migrations.RenameField(
            model_name="safeapp",
            old_name="visible",
            new_name="listed",
        ),
    ]
