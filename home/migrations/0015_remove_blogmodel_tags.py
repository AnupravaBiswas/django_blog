# Generated by Django 3.2.3 on 2021-06-03 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_blogmodel_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='tags',
        ),
    ]
