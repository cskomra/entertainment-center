import media
import fresh_tomatoes
"""This module defines objects to load on entertainment center web pages and
then calls scripts that open those pages"""


hobbit = media.Movie("The Hobit",
                     "3h 2m",
                    "The quest of home-loving hobbit Bilbo Baggins to win a share of the treasure guarded by the dragon, Smaug",
                    "http://static2.hypable.com/wp-content/uploads/2013/11/the-hobbit-the-desolation-of-smaug-poster.jpg",
                    "https://www.youtube.com/watch?v=G0k3kHtyoqc")

wonderful_life = media.Movie("It's a Wonderful Life",
                             "2h 12m",
                             "After George Bailey wishes he had never been born, an angel is sent to earth to make George's wish come true.",
                             "https://jonkuhrt.files.wordpress.com/2011/12/its-a-wonderful-life1.jpg",
                             "https://www.youtube.com/watch?v=LJfZaT8ncYk")

you_got_mail = media.Movie("You've Got Mail",
                           "1h 59m",
                          "Struggling boutique bookseller Kathleen Kelly hates Joe Fox, the owner of a corporate Foxbooks chain store that just moved in across the street.",
                          "http://ia.media-imdb.com/images/M/MV5BMTc1MzI5MTk2Ml5BMl5BanBnXkFtZTcwNDcxNzIzMQ@@._V1._SY317_CR13,0,214,317_.jpg",
                          "www.youtube.com/watch?v=znESQTt3L80")

princess_bride = media.Movie("Princess Bride",
                             "1h 38m",
                             "While home sick in bed, a young boy's grandfather reads him a story called The Princess Bride.",
                             "http://ia.media-imdb.com/images/M/MV5BMTkzMDgyNjQwM15BMl5BanBnXkFtZTgwNTg2Mjc1MDE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                             "www.youtube.com/watch?v=VYgcrny2hRs")

casablanca = media.Movie("Casablanca",
                         "1h 42m",
                         "Set in unoccupied Africa during the early days of World War II: An American expatriate meets a former lover, with unforeseen complications.",
                         "http://ia.media-imdb.com/images/M/MV5BMjQwNDYyNTk2N15BMl5BanBnXkFtZTgwMjQ0OTMyMjE@._V1_SX214_AL_.jpg",
                         "www.youtube.com/watch?v=EJvlGh_FgcI")

raiders_lost_ark = media.Movie("Raiders of the Lost Ark",
                               "1h 55m",
                               "Archaeologist and adventurer Indiana Jones is hired by the US government to find the Ark of the Covenant before the Nazis.",
                               "http://ia.media-imdb.com/images/M/MV5BMjA0ODEzMTc1Nl5BMl5BanBnXkFtZTcwODM2MjAxNA@@._V1_SX214_AL_.jpg",
                               "www.youtube.com/watch?v=0ZOcoxjeUYo")

dr_who = media.TvShow("Dr. Who",
                      "1h 0m",
                      "Creatures attack The Doctor and Clara while they are trapped on an Arctic base, and they receive help from a surprising source.",
                      "http://www.tvshowsondvd.com/graphics/news3/DoctorWho_LastChristmas_DVD.jpg",
                      "https://youtu.be/waSvCQSNruE",
                      "Season 8",
                      "Episode 13: Last Christmas",
                      "Sci-Fi")

gilligans_island = media.TvShow("Gilligan's Island",
                                "1h 0m",
                                "A beautiful Island girl becomes Gilligan's devoted servant.",
                                "http://ia.media-imdb.com/images/M/MV5BMjM1Mjg3NzU4M15BMl5BanBnXkFtZTgwNzE3ODMyMTE@._V1_SX640_SY720_.jpg",
                                "www.youtube.com/watch?v=Q8jhb5NnADM",
                                "Season 3",
                                "Episode 26: Slave Girl",
                                "CBS")

mash = media.TvShow("M*A*S*H",
                    "30 m",
                    "Members of the 4077th throw a closing party before taking down camp for the last time.",
                    "https://upload.wikimedia.org/wikipedia/en/e/ef/MASH_Goodbye.jpg",
                    "https://www.youtube.com/watch?v=FM42Sp1Pqlo",
                    "Season 11",
                    "Goodbye, Farewell and Amen",
                    "CBS")


movies = [hobbit, wonderful_life, you_got_mail, princess_bride, casablanca, raiders_lost_ark]
tvshows = [dr_who, gilligans_island, mash]
fresh_tomatoes.open_movies_page(movies)
fresh_tomatoes.create_tvshows_page(tvshows)



