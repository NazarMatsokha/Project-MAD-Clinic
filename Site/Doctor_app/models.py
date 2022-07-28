from django.db import models

class Appointment(models.Model):
    class Meta:
        unique_together = ('doctor', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '08:00 - 10:00'),
        (1, '17:00 - 20:00'),)

    doctor = models.ForeignKey('Doctor', on_delete = models.CASCADE)
    cabinet = models.ForeignKey('Location', on_delete=models.CASCADE)
    date = models.DateField(help_text="РРРР-МММ-ДД")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    patient_name = models.CharField(max_length=60)
    patient_last_name = models.CharField(max_length=60)


    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.doctor, self.patient_name)

    class Meta:
        verbose_name = "Запис на прийом"
        verbose_name_plural = "Записи на прийом"



class Location(models.Model):
    cabinet = models.CharField(help_text='Назва кабінету', max_length=50)

    def __str__(self):
        return self.cabinet

    class Meta:
        verbose_name = "Кабінет"
        verbose_name_plural = "Кабінети"



class Doctor(models.Model):
    '''Зберігає інформацію про лікаря'''


    first_name = models.CharField("Ім`я", help_text="Ім'я", max_length=20)
    last_name = models.CharField("Прізвище", help_text="Прізвище", max_length=20)
    middle_name = models.CharField("По батькові", help_text="Ім'я по батькові", max_length=20)
    speciality = models.CharField("Спеціальність", help_text="Спеціалізація", max_length=20)
    description = models.TextField("Опис", help_text="Опис спеціаліста", blank=True)
    specialist_template = models.URLField("Посилання на сторінку спеціаліста", max_length=200, blank=True)
    image = models.URLField("Фото", blank=True)

    def __str__(self):
        return '{} {}'.format(self.speciality, self.short_name)

    @property
    def short_name(self):
        return '{} {}.{}'.format(self.last_name.title(), self.first_name[0].upper(), self.middle_name[0].upper())

    class Meta:
        verbose_name = "Лікар"
        verbose_name_plural = "Лікарі"
# Create your models here.
