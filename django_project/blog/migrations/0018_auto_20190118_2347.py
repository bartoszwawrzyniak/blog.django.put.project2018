# Generated by Django 2.1.3 on 2019-01-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190118_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, default='', null=True, upload_to='media'),
        ),
    ]
