# Generated by Django 3.1.4 on 2021-01-04 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='client_id',
            new_name='client',
        ),
    ]
