# Generated by Django 3.1.5 on 2021-01-15 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numb', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=128)),
            ],
        ),
    ]
