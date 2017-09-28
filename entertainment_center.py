import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")

avatar = media.Movie("Avatar",
                     "A marine on a alien planet with blue inhabitants",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


ratatouille = media.Movie("Ratatouille",
                          "A rat that becomes a top chef",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

about_time = media.Movie("About Time",
                          "Love story about a man who can travel back in time",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA1ODUzMDA3NzFeQTJeQWpwZ15BbWU3MDgxMTYxNTk@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=T7A810duHvw")

notting_hill = media.Movie("Notting Hill",
                          "Love story between a book store owner and a famous actress",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/3/38/NottingHillRobertsGrant.jpg/220px-NottingHillRobertsGrant.jpg",
                          "https://www.youtube.com/watch?v=Ig_88q9M3SU")

les_miserables = media.Movie("Les Miserables",
                          "A story about the french revolution",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Les-miserables-movie-poster1.jpg/220px-Les-miserables-movie-poster1.jpg",
                          "https://www.youtube.com/watch?v=nQ10YRA3VKI")

movies = [toy_story, avatar, ratatouille, about_time, notting_hill, les_miserables]
fresh_tomatoes.open_movies_page(movies)

