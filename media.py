
'''
    Module: media.py
    Project: Movie Trailer Website
    Version: 1.1
    Author: Peter Majko
    Date of origin: 11/13/2015
    Last update: 11/13/2015
'''

################################################################################################################
## CLASSES
################################################################################################################

class Movie():
    '''Holds information for 1 specific movie.
Properties: .title
            .img (url of the movie poster image)
            .url (url of the youtube video)
            .year
            .director
            .writers
            .stars'''
    
    def __init__(self, title, img, yt_url, year, director, writers, stars):
        self.title = title
        self.poster_image_url = img
        self.trailer_youtube_url = yt_url
        self.year = year
        self.director = director
        self.writers = writers
        self.stars = stars


class Movies():
    '''Holds all movies added to it.
Properties: .lst (list of movies)
Methods: .add (adds movie to the .lst)
         .get_all (retrieves the list .lst)'''
    
    def __init__(self,mlist=[]):
        self.lst = mlist

    def add(self, movie):
        self.lst.append(movie)

    def get_all(self):
        return self.lst


################################################################################################################
## MAIN
################################################################################################################

if __name__ == "__main__":
    print(__doc__)
    print("<--- CLASSES ------------------------------------------->\n")
    print(str(Movie) + ":\n" + Movie.__doc__ + "\n")
    print(str(Movies) + ":\n" + Movies.__doc__ + "\n")
    print("<------------------------------------------------------->\n")

