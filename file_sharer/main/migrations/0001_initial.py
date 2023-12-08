# Generated by Django 4.1.7 on 2023-12-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('userEmail', models.EmailField(default='shaikh3@gmail.com', max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
