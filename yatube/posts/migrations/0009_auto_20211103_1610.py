# Generated by Django 2.2.9 on 2021-11-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20211103_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]