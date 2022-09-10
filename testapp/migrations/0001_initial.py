# Generated by Django 4.1.1 on 2022-09-07 09:15

import datetime
from django.db import migrations, models
import strategy_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_plan', strategy_field.fields.StrategyField(blank=True)),
                ('subscription_date', models.DateField(default=datetime.date.today)),
                ('username', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
