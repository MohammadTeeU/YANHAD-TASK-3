# Generated by Django 3.2.9 on 2021-11-16 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0007_auto_20211116_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='commerce.orderstatus', verbose_name='status'),
        ),
    ]
