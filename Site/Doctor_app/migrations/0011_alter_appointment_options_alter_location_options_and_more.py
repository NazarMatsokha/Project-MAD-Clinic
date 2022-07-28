# Generated by Django 4.0.6 on 2022-07-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor_app', '0010_doctor_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Запис на прийом', 'verbose_name_plural': 'Записи на прийом'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Кабінет', 'verbose_name_plural': 'Кабінети'},
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='title',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True, help_text='Опис спеціаліста', verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(help_text="Ім'я", max_length=20, verbose_name='Ім`я'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.URLField(blank=True, verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(help_text='Прізвище', max_length=20, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='middle_name',
            field=models.CharField(help_text="Ім'я по батькові", max_length=20, verbose_name='По батькові'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialist_template',
            field=models.URLField(blank=True, verbose_name='Посилання на сторінку спеціаліста'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(help_text='Спеціалізація', max_length=20, verbose_name='Спеціальність'),
        ),
    ]