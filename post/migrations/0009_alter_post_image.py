# Generated by Django 4.0.6 on 2022-07-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='image/post/2022-07-26-05:22:25.101747'),
        ),
    ]
