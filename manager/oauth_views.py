from django.shortcuts import render

def complete_github_view(request):
    return render(request, "complete_github.html")
