# Generated by Django 4.0.4 on 2022-04-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_subheading'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
