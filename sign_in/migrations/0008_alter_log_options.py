# Generated by Django 4.2.3 on 2023-07-20 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_in', '0007_rename_logs_log'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'permissions': (('can_view_log_history', 'can_edit_log_history'),)},
        ),
    ]
