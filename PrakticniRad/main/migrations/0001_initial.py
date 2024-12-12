# Generated by Django 5.1.2 on 2024-12-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PovrtnaBiljka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_p', models.CharField(max_length=30)),
                ('slikaBiljke_p', models.ImageField(upload_to='')),
                ('regijaBiljke_p', models.CharField(max_length=20)),
                ('vrijemeSazrijevanja_p', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='VrtnaBiljka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_v', models.CharField(max_length=30)),
                ('slikaBiljke_v', models.ImageField(upload_to='')),
                ('regijaBiljke_v', models.CharField(max_length=20)),
                ('vrijemeSazrijevanja_v', models.CharField(max_length=15)),
            ],
        ),
    ]