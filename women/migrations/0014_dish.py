# Generated by Django 4.2.1 on 2024-06-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0013_remove_reservation_number_reservation_table_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, upload_to='index')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('category', models.CharField(max_length=256)),
            ],
        ),
    ]
