# Generated by Django 3.2.8 on 2022-05-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20220525_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administration',
            options={'verbose_name': 'Администрация', 'verbose_name_plural': 'Администрация'},
        ),
        migrations.AddField(
            model_name='chronology',
            name='description_info',
            field=models.TextField(blank=True, verbose_name='Нижнее описание'),
        ),
        migrations.AlterField(
            model_name='chronology',
            name='description',
            field=models.TextField(verbose_name='Вверхние описание'),
        ),
    ]
