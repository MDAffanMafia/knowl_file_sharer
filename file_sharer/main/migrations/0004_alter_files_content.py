# Generated by Django 4.1.7 on 2023-12-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_fileaccess_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='content',
            field=models.FileField(upload_to='user_<django.db.models.fields.IntegerField>/<django.db.models.fields.CharField>'),
        ),
    ]