
'''
Module: media.py
Project: Movie Trailer Website
Version: 1.0
Author: Peter Majko
Date of origin: 11/13/2015
Last update: 11/13/2015
'''

################################################################################################################
## CLASSES
################################################################################################################

class Movie():
    def __init__(self, title, img, url, year, director, writers, stars):
        self.title = title
        self.poster_image_url = img
        self.trailer_youtube_url = url
        self.year = year
        self.director = director
        self.writers = writers
        self.stars = stars

class Movies():
    def __init__(self):
        self.lst = []

    def add(self, movie):
        self.lst.append(movie)

    def get_all(self):
        return self.lst


################################################################################################################
## MAIN
################################################################################################################

if __name__ == "__main__":
    pass
