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

def user_profile(request, id):
    # in a real app youd fetch from a database
    users = {
        1: {'name' : 'Charlie Kirk', 'email' : 'charlie@USA.com'},
        2: {'name' : 'Iqra Khan', 'email' : 'iqra552khan@gmail.com'},
        3: {'name' : 'Peter Griffin', 'email' : 'peter@gmail.com'},
        
    }

    user = users.get(id)
    if user is None:
        return render(request, 'not_found.html', {'id' : id})
    
    return render(request, 'profile.html', {'user' : user, 'id' : id})