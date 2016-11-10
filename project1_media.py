import webbrowser


class Python():
    """This application will display movie posters,We can play trailer by
    clicking it"""
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

