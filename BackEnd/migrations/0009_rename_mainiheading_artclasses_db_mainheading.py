# Generated by Django 5.0.3 on 2024-04-01 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("BackEnd", "0008_artclasses_db"),
    ]

    operations = [
        migrations.RenameField(
            model_name="artclasses_db",
            old_name="mainiheading",
            new_name="mainheading",
        ),
    ]
