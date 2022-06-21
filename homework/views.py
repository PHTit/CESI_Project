from django.shortcuts import render
from homework.models import Homework
from homework.forms import HomeworkForm
from student.views import Student
#from course.views import Course

def homeworks(request):
    #homeworks = Student.objects.all()
    homeworks = Student.objects.raw('SELECT * FROM student_student a JOIN course_course b ON a.course_id = b.id')
    
    context_dict = {
        'homeworks': homeworks
    }
    
    return render(
        request=request,
        context=context_dict,
        template_name="homework/homework_list.html"
    )

    


def homework_form(request):
    if request.method == 'POST':
        homework_form = HomeworkForm(request.POST)
        if homework_form.is_valid():
            data = homework_form.cleaned_data
            homework = Homework(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            homework.save()

            homeworks = Homework.objects.all()
            context_dict = {
                'homeworks': homeworks
            }
            return render(
                request=request,
                context=context_dict,
                template_name="homework/homework_list.html"
            )

    homework_form = HomeworkForm(request.POST)
    context_dict = {
        'homework_form': homework_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='homework/homework_form.html'
    )
