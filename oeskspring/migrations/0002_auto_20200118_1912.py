# Generated by Django 3.0.2 on 2020-01-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oeskspring', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='time',
        ),
        migrations.AddField(
            model_name='measurement',
            name='avg',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='measurement',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='measurement',
            name='enddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='measurement',
            name='failed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='measurement',
            name='iqr',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='measurement',
            name='jarname',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='measurement',
            name='median',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='measurement',
            name='namespace',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='measurement',
            name='stdev',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='measurement',
            name='times',
            field=models.IntegerField(default=1),
        ),
    ]
