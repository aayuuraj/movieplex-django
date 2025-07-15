from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Movie, Cast
from .forms import RegisterForm
from django.db.models import Q

# Home page view with search
def home(request):
    query = request.GET.get('q', '')
    movies = Movie.objects.filter(title__icontains=query) if query else Movie.objects.all()
    return render(request, 'core/home.html', {'movies': movies, 'query': query})

# Movie detail page view
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'core/movie_detail.html', {'movie': movie})

# Registration view
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})

# Like a movie (toggle like/unlike)
@login_required
def like_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user in movie.likes.all():
        movie.likes.remove(request.user)
    else:
        movie.likes.add(request.user)
    return redirect('movie_detail', pk=pk)

# Profile page: show all liked movies
@login_required
def profile_view(request):
    liked_movies = request.user.liked_movies.all()
    return render(request, 'core/profile.html', {'liked_movies': liked_movies})
