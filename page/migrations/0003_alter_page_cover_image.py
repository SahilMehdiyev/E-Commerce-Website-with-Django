# Generated by Django 4.2 on 2024-10-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='page'),
        ),
    ]