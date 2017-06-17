from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=50)


class Student(models.Model):
    name = models.CharField(max_length=10)
    # username = models.ForeignKey(Login, models.DO_NOTHING);
    age = models.IntegerField(blank=True, db_column='age of student', null=True);
