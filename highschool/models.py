# Import Django's models module which provides the base Model class and field types
from django.db import models

# Create your models here.


# Define the Student model - this represents a database table
# Each model in Django is a Python class that inherits from models.Model
class Student(models.Model):
    # GENDER_CHOICES is a list of tuples defining valid gender options
    # First value in tuple is stored in database, second value is human-readable label
    GENDER_CHOICES = [
        ('male', 'Male'),      # Store 'male' in DB, display 'Male' to user
        ('female', 'Female'),  # Store 'female' in DB, display 'Female' to user
        ('other', 'Other'),    # Store 'other' in DB, display 'Other' to user
    ]

    # CharField creates a text field with a maximum length
    # This will create a VARCHAR column in the database
    # Stores first name, max 100 characters
    firstname = models.CharField(max_length=100)
    # Stores last name, max 100 characters
    lastname = models.CharField(max_length=100)

    # IntegerField creates a field that stores integer numbers
    age = models.IntegerField()  # Stores age as a whole number

    # CharField with choices parameter creates a dropdown field
    # The choices must be one of the values defined in GENDER_CHOICES
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # DateTimeField with auto_now_add=True automatically sets the timestamp
    # when a record is first created (cannot be changed later)
    created_at = models.DateTimeField(auto_now_add=True)

    # __str__ method defines how the object is represented as a string
    # This is what you see in Django admin or when printing the object
    def __str__(self):
        return f"{self.firstname} {self.lastname}"  # Returns "John Doe" format
