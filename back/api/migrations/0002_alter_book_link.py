# Generated by Django 3.2.18 on 2023-04-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
