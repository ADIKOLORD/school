# Generated by Django 3.2.8 on 2022-05-26 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_alter_accreditation_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]
