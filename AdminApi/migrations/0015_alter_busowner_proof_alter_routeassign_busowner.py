# Generated by Django 4.2.5 on 2024-03-05 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApi', '0014_routeassign_busowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busowner',
            name='proof',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='routeassign',
            name='busowner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApi.busowner'),
        ),
    ]
