# Generated by Django 3.2.6 on 2021-09-08 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploadpic', '0003_auto_20210906_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_equipment',
            name='eq_name',
        ),
        migrations.AlterField(
            model_name='sub_equipment',
            name='volt_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_equipment_list', to='uploadpic.voltage'),
        ),
    ]
