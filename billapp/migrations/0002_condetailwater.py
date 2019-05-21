# Generated by Django 2.1.7 on 2019-05-21 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConDetailWater',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumerno', models.CharField(max_length=50)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]