# Generated by Django 4.1.7 on 2023-03-01 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudmidmorning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
