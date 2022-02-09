from django.shortcuts import render


# HTTP request
def home(request):
    return render(request, 'recipes/pages/home.html', {
        'name': 'David Castro',
    })
    
