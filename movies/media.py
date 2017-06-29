import webbrowser


class Movie(object):
    """This class provides a way to store movie-related information."""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # you can think of self as itself or the instance in question
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens a trailer for the movie from youtube"""
        webbrowser.open(self.trailer_youtube_url)


