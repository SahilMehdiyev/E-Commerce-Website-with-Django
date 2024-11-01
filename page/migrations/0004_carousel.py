# Generated by Django 4.2 on 2024-10-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_page_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_image', models.ImageField(blank=True, choices=[('draft', 'Taslak'), ('publihsed', 'Yayinlandi'), ('deleted', 'Silindi')], null=True, upload_to='page')),
                ('status', models.CharField(choices=[('draft', 'Taslak'), ('publihsed', 'Yayinlandi'), ('deleted', 'Silindi')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
