from django.shortcuts import render, redirect, get_list_or_404
#we need to import the redirect function for obvious reasons
from .forms import SnakeForm
from .models import Snake

# Create your views here.
def index(request):
    
    snakes = get_list_or_404(Snake)
    
    return render(request, 'index.html', {
        'snakes': snakes
    })

def add(request):
    
    if request.method == "POST":
        # We can process the form in here
        form = SnakeForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('snakes')
        
    else:
        form = SnakeForm
        return render(request, 'add.html', {
            'form': form
        })
    
def edit(request, snake_id):
    
    snake = Snake.objects.get(id=snake_id)
    
    if request.method == "POST":
        # We can process the form in here
        form = SnakeForm(request.POST, instance=snake)
        
        if form.is_valid():
            form.save()
        
        return redirect('snakes')
        
    else:
        form = SnakeForm
        return render(request, 'edit.html', {
            'form': form,
            'snake': snake
        })

def delete(request, snake_id):
    
    Snake.objects.get(id=snake_id).delete()
    return redirect('snakes')

def view(request, snake_id):
    
    snake = Snake.objects.get(id=snake_id)
    
    return render(request, 'view.html', {
        'snake': snake
    })
