# Generated by Django 2.1.3 on 2019-01-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]