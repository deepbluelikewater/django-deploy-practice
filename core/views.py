from django.shortcuts import render

from core.models import Student


# Create your views here.

def main(request):
    students = Student.objects.all()

    return render(request,
                'index.html',
                {'students': students,}
                  )