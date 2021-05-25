from django.shortcuts import render

#views for managing 'app'
def welcome(request):
    return render(request, "index.html")
