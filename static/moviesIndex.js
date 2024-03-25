

window.addEventListener('load', function () {
    var element = document.getElementsByClassName('movie-detail')[0];
    element.addEventListener("click", function(e) {
        debugger
        sendMovieToMovieDetail(e.currentTarget.dataset.movie);
    }, false);
    
  })

sendMovieToMovieDetail = movie => {
    // $.ajax(
    //     type: 'GET',
    //     url: 'recipe/'+recipeId,
    //     success: function (data) {
    //         window.location = "/recipe/"+recipeId;
    //     },
    //     fail: function (data) {
    //        window.location = "/error";
    //     }
    // });
    debugger

    // window.location =
    fetch('/movies/movie_detail', {
        method: 'POST',
        body: {
            "movie": movie
        },
    headers: {
          'Accept': 'application/json'
    }
    })
    .then(data =>{
        // window.location = `movies/movie_detail/${movie.name}`
    })
}
