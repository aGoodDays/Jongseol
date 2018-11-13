# Generated by Django 2.1.3 on 2018-11-13 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posture', '0003_auto_20181113_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ('date',)},
        ),
        migrations.RemoveField(
            model_name='device',
            name='datetime',
        ),
        migrations.AddField(
            model_name='device',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2018, 11, 13)),
            preserve_default=False,
        ),
    ]