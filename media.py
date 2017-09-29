import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        This definition makes all the variables in the class movie.

        :param movie_title:     (String)
        :param movie_storyline: (String)
        :param poster_image:    (String - webpage)
        :param trailer_youtube: (String - webpage)
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This method uses the webbrowser library to open the youtube trailer
        """
        webbrowser.open(self.trailer_youtube_url)
