# Generated by Django 3.1.3 on 2020-11-29 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=255, verbose_name='테스트')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_user', to=settings.AUTH_USER_MODEL, verbose_name='테스트한 유저')),
            ],
        ),
    ]
