# Generated by Django 2.2.3 on 2020-10-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geocoder', '0003_auto_20201008_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressbook',
            name='ab_id',
            field=models.CharField(editable=False, max_length=5, primary_key=True, serialize=False, unique=True),
        ),
    ]
