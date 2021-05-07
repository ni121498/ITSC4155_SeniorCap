# Generated by Django 2.2.5 on 2021-05-07 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0011_module_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheatsheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=200)),
                ('block_content', models.TextField()),
                ('cheatsheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainSite.Cheatsheet')),
            ],
        ),
    ]
