# Generated by Django 4.2.1 on 2024-05-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0006_alter_women_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='women',
            name='cat',
        ),
    ]
