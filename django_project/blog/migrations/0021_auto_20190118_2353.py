# Generated by Django 2.1.3 on 2019-01-18 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190118_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(blank=True, default='default.jpg', upload_to='media'),
        ),
    ]
