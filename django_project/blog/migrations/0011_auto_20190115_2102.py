# Generated by Django 2.1.3 on 2019-01-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190115_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='', upload_to='profile_pics'),
        ),
    ]
