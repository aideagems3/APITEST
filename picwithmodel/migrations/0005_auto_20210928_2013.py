# Generated by Django 3.2.6 on 2021-09-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picwithmodel', '0004_auto_20210928_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageformodel',
            name='Objects',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='imageformodel',
            name='Success',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='imageformodel',
            name='Time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='imageformodel',
            name='Equipmentfromuser',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]