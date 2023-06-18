# Generated by Django 4.2.2 on 2023-06-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_manga_cover_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='cover_url',
        ),
        migrations.AlterField(
            model_name='manga',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
