# Generated by Django 4.2.15 on 2024-09-01 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_categories', to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(blank=True, default='https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg', null=True),
        ),
    ]
