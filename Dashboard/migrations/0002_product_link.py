# Generated by Django 3.2 on 2022-10-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, max_length=2000),
        ),
    ]