# Generated by Django 4.0.4 on 2022-04-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('crop', models.CharField(max_length=255)),
            ],
        ),
    ]