# Generated by Django 5.0.1 on 2024-01-18 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_allmaster_rolemaster_tokenmaster_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge_bal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_recharge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_assets', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_withdrawal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('todays_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('team_income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('to_show', models.BooleanField(default=True)),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.userdetail')),
            ],
        ),
    ]
