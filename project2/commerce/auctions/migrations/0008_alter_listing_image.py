# Generated by Django 4.2.15 on 2024-08-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_rename_category_type_category_type_alter_bid_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg'),
        ),
    ]
