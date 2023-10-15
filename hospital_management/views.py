from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def custom_404(request, exception):
    context = {"message": str(exception)}
    return render(request, "404.html", context=context, status=404)
