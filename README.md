# Movie_watchlist_app
# Movie Watchlist Manager

## Description

Movie Watchlist Manager is a command-line Python application that helps users keep track of movies they want to watch, have already watched, or want to rate later. The program allows users to add movies, view their movie list, mark movies as watched, rate movies, search for movies, filter movies by genre, delete movies, and save their data.

I created this project to practice building a complete Python program using functions, lists, dictionaries, input validation, file handling, and JSON storage. The app is simple, but it is useful because it solves a real problem: keeping a personal movie watchlist organized.

## Features

The app includes the following features:

### Add Movie

The user can add a movie by entering the movie title, genre, whether they have watched it, and optionally a rating. Each movie is stored as a dictionary containing the title, genre, watched status, and rating.

### View Movies

The user can view all movies currently stored in the watchlist. The program displays the movie title, genre, watched status, and rating. If the list is empty, the program tells the user that there are no movies saved.

### Mark Movie as Watched

The user can search for a movie by title and mark it as watched. This updates the movie’s watched status from `False` to `True`.

### Rate a Movie

The user can rate a movie from 1 to 5. The program checks that the rating is a valid number within the correct range. When a movie is rated, it is also marked as watched.

### Search Movie

The user can search for a movie by title. If the movie exists in the list, the program displays its details. If the movie is not found, the program shows a message saying that the movie does not exist in the list.

### Filter by Genre

The user can filter movies based on genre. For example, the user can search for all movies in the action, comedy, drama, or sci-fi genre. The comparison is case-insensitive, so `Action`, `action`, and `ACTION` are treated the same.

### Delete Movie

The user can delete a movie from the list by entering its title. If the movie is found, it is removed from the watchlist.

### Save and Load Movies

The program saves the movie list to a JSON file called `movies.json`. When the program starts, it loads the existing movie data from this file. This allows the user’s watchlist to remain saved even after the program closes.

## Files

This project uses the following files:

* `project.py` - contains the main program and all functions.
* `movies.json` - stores the saved movie data.
* `README.md` - explains the project, features, and future plans.

## Data Structure

Each movie is stored as a dictionary. For example:

```python
{
    "title": "Interstellar",
    "genre": "Sci-Fi",
    "watched": True,
    "rating": 5.0
}
```

All movie dictionaries are stored inside a list. This makes it easy to add, view, search, filter, update, and delete movies.

## Functions

### `main()`

Starts the program. It loads saved movies from the JSON file and then opens the menu.

### `menu(movies)`

Displays the main menu and lets the user choose what action they want to perform.

### `add_movie(movies)`

Allows the user to add a new movie to the watchlist.

### `view_movies(movies)`

Displays all movies currently stored in the list.

### `mark_movie_as_watched(movies)`

Finds a movie by title and marks it as watched.

### `rate_movie(movies)`

Allows the user to rate a movie and updates the movie’s rating.

### `search_movie(movies)`

Searches for a movie by title and displays its details if found.

### `filter_by_genre(movies)`

Displays only the movies that match the genre entered by the user.

### `delete_movie(movies)`

Removes a movie from the list by title.

### `save_movies(movies)`

Saves the movie list to `movies.json`.

### `load_movies()`

Loads movie data from `movies.json`. If the file does not exist or cannot be read, the program starts with an empty list.

## Future Improvements

In the future, I would like to turn this command-line app into a GUI application. A graphical interface would make the app easier to use because users could click buttons, type into text boxes, and view their movie list in a cleaner layout.

I would also like to add a feature that can get movie information from an online movie page or movie database. For example, the user could type a movie title, and the app could automatically fetch details such as the release year, genre, rating, poster image, and description. This data could then be saved into the watchlist automatically.

For this feature, I would prefer using a movie API or a permitted data source instead of scraping pages in a way that might break website rules. This would make the app more reliable and safer to use.

Other future features could include:

* Sorting movies by rating
* Sorting movies alphabetically
* Showing only watched or unwatched movies
* Adding release year and director
* Adding movie posters
* Exporting the watchlist to a CSV file
* Creating user accounts
* Adding a GUI using Tkinter, PyQt, or a web framework

## What I Learned

While building this app, I practiced many important Python concepts, including functions, loops, dictionaries, lists, conditionals, file handling, JSON, input validation, and program organization.

This project also helped me understand how to structure a program around a menu system and how to save data so that it can be used again later.
