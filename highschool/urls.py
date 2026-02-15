# Import the path function to define URL patterns
from django.urls import path
# Import views from the current app (the dot means current package)
from . import views

# app_name creates a namespace for this app's URLs
# This allows you to reference URLs as "highschool:enroll" in templates
# Namespaces prevent URL name conflicts between different apps
app_name = "highschool"

# urlpatterns is a list of URL patterns for this app
urlpatterns = [
    # path() maps a URL pattern to a view function
    # "enroll/" - the URL path (will be /highschool/enroll/ in full)
    # views.enroll - the view function to call when this URL is accessed
    # name="enroll" - gives this URL a name for reverse lookup in templates
    path("enroll/", views.enroll, name="enroll"),
]
