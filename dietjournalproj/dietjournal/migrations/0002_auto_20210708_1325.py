# Generated by Django 3.2.3 on 2021-07-08 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dietjournal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='bedtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='logentry',
            name='sleep_quality',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='logentry',
            name='waketime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bowelmovement',
            name='day_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='date_edited',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='meal',
            name='day_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='medication',
            name='day_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='waterconsumed',
            name='day_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Sleep',
        ),
    ]
