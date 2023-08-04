# Generated by Django 3.2.20 on 2023-08-04 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_latestrelease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestrelease',
            name='image',
        ),
        migrations.RemoveField(
            model_name='latestrelease',
            name='track_details',
        ),
        migrations.AddField(
            model_name='latestrelease',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='latest_releases', to='blog.artist'),
        ),
        migrations.AlterField(
            model_name='latestrelease',
            name='download_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='latestrelease',
            name='download_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='latestrelease',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='latestrelease',
            name='vinyl_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='latestrelease',
            name='vinyl_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]