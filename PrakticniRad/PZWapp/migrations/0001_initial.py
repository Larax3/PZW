# Generated by Django 5.1.2 on 2025-02-27 21:06

import PZWapp.models
import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('lokacija', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PovrtnaBiljka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_p', models.CharField(max_length=30)),
                ('regijaBiljke_p', models.CharField(max_length=100)),
                ('vrijemeSazrijevanja_p', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VrtnaBiljka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime_v', models.CharField(max_length=30)),
                ('regijaBiljke_v', models.CharField(max_length=100)),
                ('vrijemeSazrijevanja_v', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FarmaBiljka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kolicina', models.PositiveIntegerField(default=1)),
                ('farma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='biljke_na_farmi', to='PZWapp.farma')),
                ('biljka_povrtna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PZWapp.povrtnabiljka')),
                ('biljka_vrtna', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PZWapp.vrtnabiljka')),
            ],
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('ime', models.CharField(max_length=50)),
                ('prezime', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='vrtnabiljka',
            name='user',
            field=models.ForeignKey(default=PZWapp.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, related_name='vrtne_biljke', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='povrtnabiljka',
            name='user',
            field=models.ForeignKey(default=PZWapp.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, related_name='povrtne_biljke', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='farma',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farme', to=settings.AUTH_USER_MODEL),
        ),
    ]
