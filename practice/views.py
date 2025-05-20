from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello From Django...")

def info(request):
    return HttpResponse("About Page")