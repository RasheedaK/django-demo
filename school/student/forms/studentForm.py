from django import forms

from student.models import Student


class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'rollno']
