# Generated by Django 3.2.12 on 2022-04-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findingJob', '0017_auto_20220404_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcategory',
            name='category_logo',
            field=models.ImageField(blank=True, default='defaultlogo.png', null=True, upload_to='category_logo'),
        ),
    ]
