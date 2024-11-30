from django.shortcuts import render, redirect
from .models import Course

 

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


def create_course(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        duration = request.POST["duration"]
        Course.objects.create(title=title, description=description, duration=duration)
        return redirect("course_list")

    return render(request, "courses/create_course.html")
