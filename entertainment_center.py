
"Import's media.py file"
import media

"Imports fresh_tomatoes.py file"
import fresh_tomatoes

"Each movie is built on the format described in media.py"

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life", 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", 
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

dances_with_wolves = media.Movie("Dances With Wolves",
                                 "John Dunbar befreinds wolves and Indians",
                                 "https://upload.wikimedia.org/wikipedia/en/8/82/Dances_with_Wolves_poster.jpg",
                                 "https://www.youtube.com/watch?v=J0obOvGGb1U")

i_robot = media.Movie("I Robot",
                      "A skeptical police detective, Del Spooner, stops a robotic takeover",
                      "https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg",
                      "https://www.youtube.com/watch?v=rL6RRIOZyCM")

gladiator = media.Movie("Gladiator",
                        "A betrayed roman general becomes a champion Roman Gladiator and takes revenge on the traitorous Emperor of Rome",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU")

dumb_and_dumber = media.Movie("Dumb and Dumber",
                              "Two dim-witted best friends start out on an adventure that takes them on a hillarious journey to Aspen, Colorado",
                              "https://images-na.ssl-images-amazon.com/images/I/51XVZYDA0ZL.jpg",
                              "https://www.youtube.com/watch?v=l13yPhimE3o")

"creates a list of movies in the fresh_tomatoes open_movies_page with the characteristics listed in each movie"
movies = [toy_story, avatar, dances_with_wolves, i_robot, gladiator, dumb_and_dumber]
fresh_tomatoes.open_movies_page (movies)
