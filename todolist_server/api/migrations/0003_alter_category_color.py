# Generated by Django 3.2.9 on 2021-12-02 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211202_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(max_length=9),
        ),
    ]
