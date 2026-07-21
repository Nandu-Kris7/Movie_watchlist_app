import json


def main():
    movies = load_movies()
    menu(movies)


def menu(movies):
    while True:
        print("\n1. Add Movie")
        print("2. View Movies")
        print("3. Mark movie as watched")
        print("4. Rate a movie")
        print("5. Search movie")
        print("6. Filter by genre")
        print("7. Delete movie")
        print("8. Save and Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_movie(movies)
            case "2":
                view_movies(movies)
            case "3":
                mark_movie_as_watched(movies)
            case "4":
                rate_movie(movies)
            case "5":
                search_movie(movies)
            case "6":
                filter_by_genre(movies)
            case "7":
                delete_movie(movies)
            case "8":
                save_movies(movies)
                print("Movies saved. Goodbye!")
                break   
            case _:
                print("Invalid choice. Please try again.")


def add_movie(movies):
    title = input("Enter movie title: ").strip()
    genre = input("Enter movie genre: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    if not genre:
        print("Genre cannot be empty.")
        return

    watched_input = input("Have you watched this movie? (yes/no): ").strip().lower()

    if watched_input == "yes":
        watched = True

        try:
            rating = float(input("Enter your rating for the movie (1-5): ").strip())
        except ValueError:
            print("Invalid rating. Please enter a number.")
            return

        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5.")
            return

    elif watched_input == "no":
        watched = False
        rating = None

    else:
        print("Please enter yes or no.")
        return

    movie = {
        "title": title,
        "genre": genre,
        "watched": watched,
        "rating": rating
    }

    movies.append(movie)
    print(f"{title} has been added.")


def view_movies(movies):
    if not movies:
        print("No movies in the list.")
        return

    for index, movie in enumerate(movies, start=1):
        watched = "Yes" if movie["watched"] else "No"
        rating = movie["rating"] if movie["rating"] is not None else "Not rated"

        print(f"{index}. Title: {movie['title']}, Genre: {movie['genre']}, Watched: {watched}, Rating: {rating}")


def mark_movie_as_watched(movies):
    title = input("Enter the title of the movie you want to mark as watched: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            movie["watched"] = True
            print(f"{movie['title']} has been marked as watched.")
            return

    print(f"{title} not found in the list.")


def rate_movie(movies):
    title = input("Enter the title of the movie you want to rate: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            try:
                rating = float(input("Enter your rating for the movie (1-5): ").strip())
            except ValueError:
                print("Invalid rating. Please enter a number.")
                return

            if rating < 1 or rating > 5:
                print("Rating must be between 1 and 5.")
                return

            movie["rating"] = rating
            movie["watched"] = True

            print(f"{movie['title']} has been rated {rating}.")
            return

    print(f"{title} not found in the list.")


def search_movie(movies):
    title = input("Enter the title of the movie you want to search for: ").strip()

    for movie in movies:
        if movie["title"].lower() == title.lower():
            watched = "Yes" if movie["watched"] else "No"
            rating = movie["rating"] if movie["rating"] is not None else "Not rated"

            print(f"Found movie: Title: {movie['title']}, Genre: {movie['genre']}, Watched: {watched}, Rating: {rating}")
            return

    print(f"{title} not found in the list.")


def filter_by_genre(movies):
    genre = input("Enter the genre you want to filter by: ").strip()

    if not genre:
        print("Genre cannot be empty.")
        return

    filtered_movies = [movie for movie in movies if movie["genre"].lower() == genre.lower()]

    if not filtered_movies:
        print(f"No movies found in the genre: {genre}.")
    else:
        view_movies(filtered_movies)


def delete_movie(movies):
    title = input("Enter the title of the movie you want to delete: ").strip()
    for movie in movies:
        if movie['title'].lower() == title.lower():
            movies.remove(movie)
            print(f"{title} has been deleted from the list.")
            return
    print(f"{title} not found in the list.")


def save_movies(movies):
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)


def load_movies():
    try:
        with open("movies.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error loading movies. Starting with an empty list.")
        return []


if __name__ == "__main__":
    main()