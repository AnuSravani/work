# Generated by Django 4.2.3 on 2023-07-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RobertCategorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roberts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('robert_name', models.CharField(max_length=100)),
                ('currency', models.CharField(choices=[('INR', 'INR'), ('DOLLAR', 'DOLLAR'), ('RIYAL', 'RIYAL')], default='INR', max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('manufacture_date', models.DateField(auto_now_add=True)),
                ('manufacture_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mname', to='api.manufacturers')),
                ('robert_cate_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rcategory', to='api.robertcategorys')),
            ],
        ),
    ]
