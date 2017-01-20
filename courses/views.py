from django.http import HttpResponse
from django.shortcuts import render

from .models import Courses


def course_list(request):
    courses = Courses.objects.all()
    output = ', '.join([str(course) for course in courses])
    return HttpResponse(output)
