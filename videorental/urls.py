from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.views.generic import ListView, DetailView
from videorental.models import Movie
from bodebusters import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.screen_init, name='screen_init'), # Home button, first screen
    path('movies/', ListView.as_view(queryset = Movie.objects.all().order_by('title'), template_name = 'videorental/movies.html')), # Movies button
    path('rented/', ListView.as_view(queryset = Movie.objects.all().order_by('title'), template_name = 'videorental/rented.html')), # Out of stock button
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'), # login button on first screen
    path('my_movies/', views.my_movie, name='my_movies'), # my movies screen
    path('sign_up/', views.SignUp.as_view(), name='signup'), # sign up button on first screen
    re_path(r'^rent/(?P<pk_user>(\d+))/(?P<pk_m>(\d+))', views.rent, name='rent_movie'), # rent button on movies screen
    re_path(r'^give_back/(?P<pk_user>(\d+))/(?P<pk_m>(\d+))', views.give_back, name='give_back_movie'), # give back button on rented screen
    re_path(r'(?P<pk>(\d+))', DetailView.as_view(model = Movie, template_name = 'videorental/moviedetail.html')) # link for the movie details
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


