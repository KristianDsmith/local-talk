# Generated by Django 3.2.20 on 2023-08-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_record_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='category',
            field=models.CharField(choices=[('ALBUM', 'Album'), ('LATEST', 'Latest Release'), ('SINGLE', 'Single')], default='LATEST', max_length=10),
        ),
    ]
