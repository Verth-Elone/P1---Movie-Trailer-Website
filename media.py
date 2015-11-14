'''
    Module: media.py
    Project: Movie Trailer Website
    Version: 1.2
    Author: Peter Majko
    Date of origin: 11/13/2015
    Last update: 11/14/2015
'''

# CLASSES


class Movie():
    '''Holds information for 1 specific movie.

    Attributes: .title (str)
                .img (str): url of the movie poster image
                .url (str): url of the youtube video
                .year (str)
                .genre (str)
                .director (str)
                .writers (str)
                .stars (str)

    __init__ requires all above attributes
    '''

    def __init__(self, title, img, yt_url, year,
                 genre, director, writers, stars):
        self.title = title
        self.poster_image_url = img
        self.trailer_youtube_url = yt_url
        self.year = year
        self.genre = genre
        self.director = director
        self.writers = writers
        self.stars = stars


class Movies():
    '''Holds all movies added to it.

    Attributes: .lst (list): list of instances of class Movie

    Methods:    .add (adds movie to the .lst)
                .get_all (retrieves the list .lst)
    '''

    def __init__(self, mlist=[]):
        # using list instead of tuple to be able to insert new movie
        # on the fly, for possible future of the project
        self.lst = mlist

    def add(self, movie):
        '''Appends instance of class Movie to self.lst'''
        self.lst.append(movie)

    def get_all(self):
        '''Returns list of instances of class Movie stored in self.lst'''
        return self.lst


# MAIN

if __name__ == "__main__":
    print(__doc__)
    print("<--- CLASSES ------------------------------------------->\n")
    print(str(Movie) + ":\n" + Movie.__doc__ + "\n")
    print(str(Movies) + ":\n" + Movies.__doc__ + "\n")
    print("<------------------------------------------------------->\n")
