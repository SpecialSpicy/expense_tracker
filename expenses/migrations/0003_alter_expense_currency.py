# Generated by Django 5.0.7 on 2024-07-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_expense_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='currency',
            field=models.CharField(blank=True, default='USD', max_length=3, null=True),
        ),
    ]