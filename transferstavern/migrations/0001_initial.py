# Generated by Django 4.2.11 on 2024-04-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transferstavern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField(max_length=250)),
                ('image_url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
