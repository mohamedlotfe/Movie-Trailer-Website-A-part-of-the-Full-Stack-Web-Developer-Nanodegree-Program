import webbrowser
class Movie():
    """ this the documentaion about  the movie class   """
    VALID_RATING=["G","VG","PG-13","R"]

    def __init__(self,movie_title,movie_story,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)