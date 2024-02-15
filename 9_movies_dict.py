# Create a dictionary with at least ten movies and a rating out of ten
movies = {
    "Inception": 6.8,
    "The Dark Knight": 9.0,
    "The Godfather": 9.2,
    "Pulp Fiction": 5.9,
    "The Shawshank Redemption": 9.3,
    "The Avengers": 7.0,
    "Guardians of the Galaxy": 8.0,
    "Iron Man": 7.9,
    "The Lord of the Rings": 8.8,
    "Jurassic Park": 7.5,
    "Avatar": 7.8,
    "Deadpool": 3.0,
    "Spider-Man: Into the Spider-Verse": 8.4,
    "Black Panther": 7.3,
    "Avengers: Endgame": 8.4
}

#Ask the user for a movie title. 
movie_title = input("Please Enter a Movie Title: ")

#Write a function named recommend_movie that takes the movie_rating dictionary and the movie title as arguments.
def recommend_movie(movies, movie_title):
    if movie_title in movies and movies[movie_title] > 8:
        print(f"Great Choice! {movie_title} is rated {movies[movie_title]}, Enjoy the Show :)")
    
    elif movie_title in movies and movies[movie_title] < 8:
        print()
        print(f"{movie_title} Is rated: {movies[movie_title]}. Try one of these movies with a 8 or higher rating:\n")
        for movie, rating in movies.items():
            if rating >= 8:
                print(f"{movie}: {rating}")
    else:
        print()
        print(f"Sorry, I don't have a rating for {movie_title}")
        print(f"Try one of these movies with a 8 or higher rating:")
        for movie, rating in movies.items():
            if rating >= 8:
                print(f"{movie}: {rating}")


recommend_movie(movies, movie_title)