import media
import fresh_tomatoes

'''
Module: entertainment_center.py
Project: Movie Trailer Website
Version: 1.0
Author: Peter Majko
Date of origin: 11/13/2015
Last update: 11/13/2015

PROPRIETARY:
    Movie titles are taken from IMDB.com
    Poster URLs are taken from IMDB.com
    Video links are taken from YouTube.com
'''

################################################################################################################
## MAIN
################################################################################################################

if __name__ == "__main__":
    movies = media.Movies()
    m1 = media.Movie("Star Wars: Episode VII - The Force Awakens",
                     "http://ia.media-imdb.com/images/M/MV5BMTkwNzAwNDA4N15BMl5BanBnXkFtZTgwMTA2MDcwNzE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                     "2015",
                     "J.J. Abrams",
                     "Lawrence Kasdan, J.J.Abrams, Michael Arndt, Goerge Lucas",
                     "Harrison Ford, Mark Hamill, Carrie Fisher, ...")
    m2 = media.Movie("Warcraft",
                     "http://ia.media-imdb.com/images/M/MV5BMTgxMDAzNzMyMV5BMl5BanBnXkFtZTgwNjIwMTgxNzE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=2Rxoz13Bthc",
                     "2016",
                     "Duncan Jones",
                     "Duncan Jones, Charles Leavitt, Chris Metzen",
                     "Travis Fimmel, Dominic Cooper, Paula Patton, ...")
    m3 = media.Movie("Jurassic World",
                     "http://ia.media-imdb.com/images/M/MV5BMTQ5MTE0MTk3Nl5BMl5BanBnXkFtZTgwMjczMzk2NTE@._V1_SX214_AL_.jpg",
                     "https://www.youtube.com/watch?v=ZXiahojLbOw",
                     "2015",
                     "Colin Trevorrow",
                     "DRick Jaffa, Amanda Silver, ...",
                     "Chris Pratt, Bryce Dallas Howard, Ty Simpkins, ...")
    m4 = media.Movie("Avatar",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "2009",
                     "James Cameron",
                     "James Cameron",
                     "Sam Worthington, Zoe Saldana, Sigourney Weaver, ...")
    movies.add(m1)
    movies.add(m2)
    movies.add(m3)
    movies.add(m4)
    fresh_tomatoes.open_movies_page(movies.get_all())
