# Generated by Django 3.2.2 on 2021-06-02 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='HarriBlog', max_length=255),
        ),
    ]
