from django.shortcuts import render, redirect
from .models import Student

def index(request):
    if request.method == "POST":
        Student.objects.create(
            full_name=request.POST.get("full_name"),
            date_of_birth=request.POST.get("date_of_birth"),
            subject=request.POST.get("subject"),
            enrollment_year=request.POST.get("enrollment_year"),
            highschool_cgpa=request.POST.get("highschool_cgpa"),
            eca_interest=request.POST.get("eca_interest"),
            eca_choice=request.POST.get("eca_choice"),
            reason=request.POST.get("reason"),
        )
        return redirect("index")  # refresh page after submit

    return render(request, "students/index.html")

