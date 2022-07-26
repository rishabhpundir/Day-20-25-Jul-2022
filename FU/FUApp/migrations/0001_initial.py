# Generated by Django 3.2.4 on 2022-07-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=1)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Profile Photo')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='User Description')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
