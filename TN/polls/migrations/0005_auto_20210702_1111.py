# Generated by Django 3.2.4 on 2021-07-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210702_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='inboundpartialdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='outboundpartialdate',
            field=models.DateField(),
        ),
    ]
