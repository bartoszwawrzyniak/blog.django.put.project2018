# Generated by Django 2.1.3 on 2019-01-18 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190118_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
