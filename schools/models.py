from django.db import models


# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=100)
    school_href = models.CharField(max_length=150)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = "schools"

class Department(models.Model):
    dpt_name = models.CharField(max_length=100, unique=False)
    dpt_href = models.CharField(max_length=150)
    # Foreignkey 不确定关系的 用字符串表示（类）
    school = models.ForeignKey('School',on_delete=models.CASCADE,related_name='dpts')

    class Meta:
        db_table = "departments"


class Tutor(models.Model):
    tutor_name = models.CharField(max_length=100, unique=False)
    tutor_href = models.CharField(max_length=150)
    # Foreignkey 不确定关系的 用字符串表示（类）
    comment= models.CharField(max_length=240)
    student= models.CharField(max_length=100)
    dpt=models.ForeignKey('Department',on_delete=models.CASCADE,related_name='tutors')
    school = models.ForeignKey('School',on_delete=models.CASCADE,related_name='tutors')

    class Meta:
        db_table = "tutors"