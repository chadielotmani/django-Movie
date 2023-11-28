document.getElementById('change-movie-button').addEventListener('click', function() {
    var imdbId = this.getAttribute('data-imdb');
    var movieUrl = 'https://vidsrc.me/embed/movie?imdb=tt' + imdbId;
  
    var iframe = document.getElementById('iframe-embed');
    iframe.src = movieUrl;
  });