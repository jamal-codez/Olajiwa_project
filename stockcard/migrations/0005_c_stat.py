# Generated by Django 4.2.1 on 2023-06-03 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockcard', '0004_alter_stock_card_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='C_stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advance', models.FloatField(blank=True, null=True)),
                ('Out', models.FloatField(null=True)),
                ('paid', models.FloatField(null=True)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stockcard.customers')),
            ],
        ),
    ]
