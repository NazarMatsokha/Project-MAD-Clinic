# Generated by Django 4.0.6 on 2022-08-10 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Specialist_app', '0003_alter_comments_options_alter_comments_specialist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='status',
        ),
    ]
