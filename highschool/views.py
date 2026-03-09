
from django.shortcuts import render

from . models import Student

def enroll(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        age = request.POST.get("age", "").strip()
        gender = request.POST.get("gender", "").strip()

        student = Student.objects.create(
            firstname=firstname,  # Set firstname field
            lastname=lastname,    # Set lastname field
            # Convert age string to integer, use 0 if empty
            age=int(age) if age else 0,
            gender=gender         # Set gender field
        )

        info = {
            "submitted": True,     # Flag to show success message in template
            "firstname": firstname,  # Pass firstname to template 
            "lastname": lastname,    # Pass lastname to template 
            "age": age,              # Pass age to template
            "gender": gender,        # Pass gender to template
        }
       
        return render(request, "enroll.html", info)
    return render(request, "enroll.html")
