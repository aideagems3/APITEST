# Generated by Django 3.2.6 on 2021-09-30 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picwithmodel', '0007_imageformodel_boxespic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageformodel',
            name='Boxespic',
        ),
    ]
