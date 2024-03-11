# Generated by Django 4.2.5 on 2024-03-02 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApi', '0009_bus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busstop',
            old_name='name',
            new_name='stop_name',
        ),
        migrations.AddField(
            model_name='busstop',
            name='approx_cost',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='busstop',
            name='time_taken',
            field=models.TimeField(null=True),
        ),
        migrations.CreateModel(
            name='RouteAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApi.bus')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApi.route')),
            ],
        ),
    ]