# Generated by Django 3.2.6 on 2021-09-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picwithmodel', '0002_auto_20210928_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageformodel',
            name='Success',
            field=models.BooleanField(default=False),
        ),
    ]