# Generated by Django 3.2.20 on 2023-08-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_record_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='download_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='record',
            name='download_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='vinyl_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='record',
            name='vinyl_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='category',
            field=models.CharField(blank=True, choices=[('ALBUM', 'Album'), ('LATEST', 'Latest Release'), ('SINGLE', 'Single')], default='LATEST', max_length=10),
        ),
    ]
