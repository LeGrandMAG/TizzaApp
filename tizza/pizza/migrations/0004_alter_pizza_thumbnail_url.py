# Generated by Django 4.0.3 on 2022-03-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_alter_pizza_thumbnail_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='thumbnail_url',
            field=models.URLField(default='google.com', null=True),
        ),
    ]
