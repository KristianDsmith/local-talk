# Generated by Django 3.2.20 on 2023-08-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_record_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='category',
            field=models.CharField(blank=True, choices=[('ALBUM', 'Album'), ('LATEST', 'Latest Release'), ('SINGLE', 'Single')], default='LATEST', max_length=10),
        ),
    ]
