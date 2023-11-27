from django.http import HttpResponse


def home(request):
    return Httpresponse("This is Homepage")

def contact(request):
    return HttpResponse("This is Contact page")
    