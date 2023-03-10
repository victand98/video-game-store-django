# Generated by Django 4.1.7 on 2023-03-04 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('price_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.game')),
            ],
        ),
    ]
