# Generated by Django 4.2.5 on 2024-03-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApi', '0012_alter_route_ends_at_alter_route_starts_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdriver',
            name='license',
            field=models.ImageField(upload_to='image'),
        ),
    ]
