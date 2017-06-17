from django.db import models

# Create your models here.
class Student(models.Model):
    class Meta:
        db_table = 'student'
    name = models.CharField(max_length=10)
    # username = models.ForeignKey(Login, models.DO_NOTHING);
    age = models.IntegerField(blank=True, db_column='age of student', null=True);
    rollno = models.IntegerField(blank=True,null=True,db_column='roll_no')