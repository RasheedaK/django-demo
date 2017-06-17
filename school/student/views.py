from django.shortcuts import render, redirect

# Create your views here.
from student.forms.studentForm import studentForm


def viewForm(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return render(request, 'save.html', {'name': student.name})
    else:
        form = studentForm()
    return render(request, 'student.html', {'student_form': form})

