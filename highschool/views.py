# Import render function to display HTML templates
from django.shortcuts import render
# Import the Student model from the current app's models.py file
# The dot (.) means "current package/app"
from .models import Student

# Create your views here.


# Define the enroll view function that handles the enrollment page
# Every view receives a request object containing information about the HTTP request
def enroll(request):
    # Check if the form was submitted (POST request means form submission)
    # GET request means user is just viewing the page
    if request.method == "POST":
        # Extract form data from request.POST dictionary
        # .get() method safely retrieves value, returns empty string if not found
        # .strip() removes whitespace from beginning and end of the string
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        age = request.POST.get("age", "").strip()
        gender = request.POST.get("gender", "").strip()

        # Save the student data to the database
        # Student.objects.create() creates a new record and saves it in one step
        student = Student.objects.create(
            firstname=firstname,  # Set firstname field
            lastname=lastname,    # Set lastname field
            # Convert age string to integer, use 0 if empty
            age=int(age) if age else 0,
            gender=gender         # Set gender field
        )

        # Create a context dictionary to pass data to the template
        # This allows the template to display the submitted information
        context = {
            "submitted": True,     # Flag to show success message in template
            "firstname": firstname,  # Pass firstname to template
            "lastname": lastname,    # Pass lastname to template
            "age": age,              # Pass age to template
            "gender": gender,        # Pass gender to template
        }
        # Render the template with the context data and return the response
        return render(request, "enroll.html", context)

    # If request method is GET (user just visiting the page),
    # render the empty form without any context data
    return render(request, "enroll.html")
