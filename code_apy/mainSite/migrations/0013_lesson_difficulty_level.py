# Generated by Django 2.2.5 on 2021-05-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0012_block_cheatsheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='difficulty_level',
            field=models.CharField(default='easy', max_length=200),
        ),
    ]