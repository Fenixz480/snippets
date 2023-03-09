# Generated by Django 4.1.1 on 2023-02-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_snippet_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='access',
            field=models.CharField(choices=[('public', 'public'), ('private', 'private')], default='public', max_length=30),
        ),
    ]