# Generated by Django 2.1.1 on 2018-11-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapi', '0010_auto_20181114_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default='PracticaEstructura', max_length=50),
        ),
    ]
