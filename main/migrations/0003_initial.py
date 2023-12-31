# Generated by Django 4.2.6 on 2023-10-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('image_s', models.URLField(blank=True, null=True)),
                ('image_m', models.URLField(blank=True, null=True)),
                ('image_l', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
