# Generated by Django 4.0.6 on 2022-08-08 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Specialist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Коментарій')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата створення')),
                ('status', models.BooleanField(default=False, verbose_name='Статус статті')),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('specialist', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_specialist', to='Specialist_app.specialist')),
            ],
            options={
                'verbose_name': 'Коментарій',
                'verbose_name_plural': 'Коментарії',
            },
        ),
    ]
