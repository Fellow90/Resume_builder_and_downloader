# Generated by Django 4.2.3 on 2023-08-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_personalinformation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='title',
            field=models.CharField(max_length=8),
        ),
    ]
