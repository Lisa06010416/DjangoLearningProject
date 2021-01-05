from django.db import models

# Create your models here.


class Book(models.Model):
    b_id = models.AutoField(auto_created=True, primary_key=True, verbose_name='b_id')
    book_name = models.TextField(default=None)
    title = models.TextField(default=None)
    author_name = models.TextField(default=None)


class Person(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    name = models.TextField()

    class Meta:
        abstract = True


class Teacher(Person):
    teacher_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'Teacher'


class Student(Person):
    student_id = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, related_name='has_student', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Student'
