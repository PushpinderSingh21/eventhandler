# Generated by Django 2.2 on 2019-05-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0012_participate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createevent',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='createevent',
            name='registered',
            field=models.CharField(default='False', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='participate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
