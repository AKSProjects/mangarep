# Generated by Django 4.2.2 on 2023-06-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('manga_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=252)),
                ('type', models.CharField(max_length=11)),
                ('score', models.CharField(blank=True, max_length=18, null=True)),
                ('scored_by', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('volumes', models.IntegerField(blank=True, null=True)),
                ('chapters', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('members', models.IntegerField()),
                ('favorites', models.IntegerField()),
                ('sfw', models.CharField(max_length=5)),
                ('approved', models.CharField(max_length=5)),
                ('created_at_before', models.CharField(max_length=32)),
                ('updated_at', models.CharField(blank=True, max_length=25, null=True)),
                ('real_start_date', models.CharField(blank=True, max_length=10, null=True)),
                ('real_end_date', models.CharField(blank=True, max_length=10, null=True)),
                ('genres', models.CharField(max_length=113)),
                ('themes', models.CharField(max_length=102)),
                ('demographics', models.CharField(max_length=21)),
                ('authors', models.CharField(max_length=4554)),
                ('serializations', models.CharField(max_length=49)),
                ('synopsis', models.CharField(blank=True, max_length=4583, null=True)),
                ('background', models.CharField(blank=True, max_length=4454, null=True)),
                ('main_picture', models.CharField(blank=True, max_length=54, null=True)),
                ('url', models.CharField(max_length=236)),
                ('title_english', models.CharField(blank=True, max_length=207, null=True)),
                ('title_japanese', models.CharField(blank=True, max_length=98, null=True)),
                ('title_synonyms', models.CharField(max_length=295)),
                ('jikan', models.CharField(max_length=5)),
            ],
        ),
    ]