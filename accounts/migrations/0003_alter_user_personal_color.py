# Generated by Django 3.2.2 on 2021-05-23 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_personal_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='personal_color',
            field=models.CharField(default='', max_length=50),
        ),
    ]
