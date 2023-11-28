from django.shortcuts import render
import requests
from .models import Movie

def search_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')  # Assuming the form input name is 'title'
        api_key = '15d2ea6d0dc1d476efbca3eba2b9bbfb'  # Replace with your movie database API key

        # Make a request to the movie database API
        api_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}'
        response = requests.get(api_url)

        if response.status_code == 200:
            movie_data = response.json()
            if movie_data['results']:
                movie_info = movie_data['results'][0]  # Assuming we take the first result
                poster = f"https://image.tmdb.org/t/p/original{movie_info['poster_path']}"
                overview = movie_info['overview']
                release_date = movie_info['release_date']

                # Save movie information to your Django model
                Movie.objects.create(
                    title=title,
                    poster=poster,
                    overview=overview,
                    release_date=release_date,
                )

                return render(request, 'movie_details.html', {
                    'title': title,
                    'poster': poster,
                    'overview': overview,
                    'release_date': release_date,
                })

    return render(request, 'search_movie.html')