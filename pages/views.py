from django.shortcuts import render

# Create your views here.

def home(request):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    username = request.GET.get('username', 'GUest')
    return render(request, 'home.html', {
        'username': username,
        'title' : 'Welcomeee',
        'items' : ['carrot', 'turnip', 'tomato'],
        'numbers' : numbers,
        })

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')