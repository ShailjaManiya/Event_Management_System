# Generated by Django 4.0 on 2022-01-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeEventful', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
            ],
        ),
    ]
