from django.db import models
from students.models import Student
from teachers.models import Teacher


# Create your models here.
class_choices = (
    ('Django'),
    ('Ralavel'),
    ('React'),
    ('Node js'),
)

class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)
class Attendance(models.Model):
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)
    date = models.DateField()
    mark_attendance = models.CharField(max_length=50, choices=class_attendance)

# Create your models here.
