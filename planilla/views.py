from django.shortcuts import render
from student.views import Student

def planilla(request):
    
    planilla = Student.objects.raw('SELECT * FROM student_student a JOIN course_course b ON a.course_id = b.id')
    
    context_dict = {
        'planilla': planilla
    }
    
    return render(
        request=request,
        context=context_dict,
        template_name="planilla/planilla.html"
    )


