# Generated by Django 2.1.3 on 2019-01-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190115_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='new.jpg', upload_to='profile_pics'),
        ),
    ]
