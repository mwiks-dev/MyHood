# Generated by Django 3.2.9 on 2022-01-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0013_auto_20220111_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='hood_name',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]