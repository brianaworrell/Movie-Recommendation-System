# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    ratings = {}
    for line in open(f):
        parts = line.split('|')
        moviename = parts[0].strip()
        if moviename in ratings:
            ratings[moviename].append(float(parts[1].strip()))
        else:
            ratings[moviename] = [float(parts[1].strip())]
    return ratings
    

# 1.2
def read_movie_genre(f):
    genres = {}
    for line in open(f):
        parts = line.split('|')
        moviename = parts[2].strip()
        genres[moviename] = parts[0].strip()
    return genres

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    genres = {}
    for movie in d:
        if d[movie] in genres:
            genres[d[movie]].append(movie)
        else:
            genres[d[movie]] = [movie]
    return genres
    
# 2.2
def calculate_average_rating(d):
    averagerating = {}
    for movie in d:
        average = sum(d[movie])/len(d[movie])
        averagerating[movie] = average
    return averagerating
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    ranked = {}
    sorteddict = sorted(d, key=d.get)
    sorteddict.reverse()
    numresults = n
    if len(sorteddict) < n:
        numresults = len(sorteddict)
    for x in range(0,numresults):
        ranked[sorteddict[x]] = d.get(sorteddict[x])
    return ranked
    
# 3.2
def filter_movies(d, thres_rating=3):
    filtered = {}
    for movie in d:
        if d[movie] >= thres_rating:
            filtered[movie] = d[movie]
    return filtered
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    ingenre = genre_to_movies[genre]
    ingenredict = {}
    for movie in ingenre:
        ingenredict[movie] = movie_to_average_rating[movie]
    ranked = get_popular_movies(ingenredict, n)
    return ranked
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    ingenre = genre_to_movies[genre]
    sumrate = 0
    movies = 0
    for movie in ingenre:
        sumrate = sumrate + movie_to_average_rating[movie]
        movies = movies + 1
    average = sumrate/movies
    return average
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    genreratings = {}
    for genre in genre_to_movies:
        genreratings[genre] = get_genre_rating(genre, genre_to_movies, movie_to_average_rating)
    ranked = get_popular_movies(genreratings, n)
    return ranked

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    users = {}
    for line in open(f):
        parts = line.split('|')
        userid = int(parts[2].strip())
        movie = parts[0].strip()
        rating = float(parts[1].strip())
        if userid in users:
            users[userid].append((movie, rating))
        else:
            users[userid] = [(movie, rating)]
    return users
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    userratings = user_to_movies[user_id]
    genres = {}
    for x in userratings:
        rating = x[1]
        movie = x[0] 
        thisgenre = movie_to_genre[movie]
        if thisgenre in genres:
            genres[thisgenre].append(rating)
        else:
            genres[thisgenre] = [rating]
    genrerates = {}
    for genre in genres:
        average = sum(genres[genre])/len(genres[genre])
        genrerates[genre] = average
    ranked = sorted(genrerates, key=genrerates.get)
    ranked.reverse()
    return ranked[0] 
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    fav = get_user_genre(user_id, user_to_movies, movie_to_genre)
    ingenre = {}
    for movie in movie_to_genre:
        if movie_to_genre[movie] == fav:
            rating = movie_to_average_rating[movie]
            ingenre[movie] = rating
    rated = user_to_movies[user_id]
    for x in rated:
        if x[0] in ingenre:
            del ingenre[x[0]]
    ranked = sorted(ingenre, key = ingenre.get)
    ranked.reverse()
    top3 = {}
    stop = 3
    if len(ranked) < 3:
        stop = len(ranked)
    for y in range(0,stop):
        top3[ranked[y]] = movie_to_average_rating[ranked[y]]
    return top3   

# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading
    pass
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()
