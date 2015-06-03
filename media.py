import webbrowser

class Video():
    """This class provides a way to store video related information."""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """This class provides a way to store movie related information."""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"];  

    def __init__(self, title, duration, storyline, image, trailer):
        Video.__init__(self, title, duration)        
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        

class TvShow(Movie):
    """This class provides a way to store TV show related information."""

    def __init__(self, title, duration, storyline, image, trailer, season, episode, station):
        Movie.__init__(self, title, duration, storyline, image, trailer)
        self.season = season
        self.episode = episode
        self.station = station
        


