# Generated by Django 2.1.3 on 2018-11-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posture', '0005_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_id',
            field=models.IntegerField(),
        ),
    ]