import webbrowser
class Movies():
    def __init__(self,movie_title,movie_director,movie_ratings,movie_poster_image,movie_trailer_youtube):
        self.title=movie_title
        self.director=movie_director
        self.ratings=movie_ratings
        self.poster_image_url=movie_poster_image
        self.trailer_youtube_url=movie_trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
