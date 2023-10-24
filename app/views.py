from django.shortcuts import render


def home(request):
    content = {
        's': 'Hello, World!'
    }

    return render(request, 'home.html', content)
