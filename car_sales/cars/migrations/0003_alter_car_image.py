# Generated by Django 5.0.6 on 2024-06-10 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0002_alter_car_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/cars/"),
        ),
    ]