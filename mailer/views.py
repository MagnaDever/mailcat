from django.shortcuts import render


def index(request):
 #   response.headers.delete('X-Frame-Options')
    return render(response.headers.delete('X-Frame-Options'), 'index.html', {})
