# Generated by Django 3.2.23 on 2024-01-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('password', models.TextField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
