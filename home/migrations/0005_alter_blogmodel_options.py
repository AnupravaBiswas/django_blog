# Generated by Django 3.2.3 on 2021-05-30 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210529_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ['-created_at']},
        ),
    ]
