# Generated by Django 3.2.4 on 2021-07-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210702_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='country',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='inboundpartialdate',
            field=models.DateField(blank=True),
        ),
    ]
