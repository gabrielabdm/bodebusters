from django.shortcuts import render, redirect
from videorental.models import Movie, RentedMovie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

def screen_init(request):
    return render(request, 'videorental/screeninit.html')


def login(request):
    return render(request, 'videorental/login.html')


def movies(request):
    return render(request, 'videorental/movies.html')


def rented(request):
    return render(request, 'videorental/rented.html')


def rent(request, pk_user, pk_m):
    movie = Movie.objects.get(pk=pk_m)
    movie.rent()
    movie.save()
    user = User.objects.get(pk=pk_user)
    already_rented = False
    for user_rented_movie in user.profile.rented_movies.all():
        if user_rented_movie.movie.id == movie.id:
            print('\nEntrei no if\n')
            user_rented_movie.quantity += 1
            user_rented_movie.save()
            already_rented = True
            break
    if not already_rented:
        print('\nEntrei no if not\n')
        rentedMovie = RentedMovie(
            movie = movie,
            quantity = 1
        )
        print(rentedMovie)
        rentedMovie.save()
        user.profile.rented_movies.add(rentedMovie)
    user.save()
    print(user.profile.rented_movies.all())
    return redirect('../../movies/')


def give_back(request, pk_user, pk_m):
    movie = Movie.objects.get(pk=pk_m)
    movie.give_back()
    movie.save()
    user = User.objects.get(pk=pk_user)
    for user_rented_movie in user.profile.rented_movies.all():
        if user_rented_movie.movie.id == movie.id:
            print('\nDiminuindo quantidade\n')
            user_rented_movie.quantity -= 1
            user_rented_movie.save()
            if user_rented_movie.quantity == 0:
                print('\nDeletando\n')
                user.profile.rented_movies.remove(user_rented_movie)
                user_rented_movie.delete()
            break
    user.save()
    return redirect('../../my_movies/')


def my_movie(request):
    return render(request, 'videorental/my_movies.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'