# Generated by Django 4.0.4 on 2022-12-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='users/django.png', max_length=250, null=True, upload_to='users'),
        ),
    ]