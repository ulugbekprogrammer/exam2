# Generated by Django 5.0.3 on 2024-03-18 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_emailmessage_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailmessage',
            name='sent_at',
            field=models.EmailField(max_length=254),
        ),
    ]
