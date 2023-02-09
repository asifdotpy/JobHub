# Generated by Django 4.1.6 on 2023-02-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalMarketingManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/digital_marketing_managers/')),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FullStackDeveloper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/full_stack_developers/')),
                ('area', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]
