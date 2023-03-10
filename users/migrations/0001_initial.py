# Generated by Django 4.0.4 on 2022-12-14 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_day', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, default='users.django.png', max_length=250, null=True, upload_to='users')),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
