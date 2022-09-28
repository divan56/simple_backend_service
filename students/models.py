from django.db import models


class Student(models.Model):
    # Факультеты
    COLLEGE_CHOICES = [
        ('MED', 'Medical'),
        ('IT', 'Information Technologies'),
        ('JUR', 'Juridic')
    ]

    name = models.TextField()  # Имя
    course = models.IntegerField()  # Курс, на котором учится студент
    college = models.CharField(max_length=3, choices=COLLEGE_CHOICES)  # Факультет, на котором учится студент
    date_of_birth = models.DateField()  # Дата рождения студента в формате ГГГГ-ММ-ДД (1978-04-07)
    studies_from = models.DateField(
        auto_now_add=True)  # Дата, с которой студент занесен в БД (назначается автоматически, когда студент создается)
