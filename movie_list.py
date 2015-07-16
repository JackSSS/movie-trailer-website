import media
import fresh_tomatoes

# Class attributes to movie names.
guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "A group of intergalactic criminals are "
                                      "forced to work together to stop a "
                                      "fanatical warrior from taking control "
                                      "of the universe.",
                                      "http://metrouk2.files.wordpress.com/2014/02/ad_127934252.jpg?w=692&quality=80&strip=all&h=1024",
                                      "https://www.youtube.com/watch?v=B16Bo47KS2g")

skyfall = media.Movie("Skyfall",
                      "Bond's loyalty to M is tested when her past comes back "
                      "to haunt her. Whilst MI6 comes under attack, 007 must "
                      "track down and destroy the threat, no matter how "
                      "personal the cost.",
                      "http://api.comingsoon.net//images//2012/Skyfall_62.jpg",
                      "https://www.youtube.com/watch?v=6kw1UVovByw")

seven = media.Movie("Se7en",
                    "Two detectives, a rookie and a veteran, "
                    "hunt a serial killer who uses the seven deadly sins "
                    "as his modus operandi.",
                    "http://files.sharenator.com/seven_movie_poster_500w-s500x730-30770-580.jpg",
                    "https://www.youtube.com/watch?v=J4YV2_TcCoE")

snatch = media.Movie("Snatch",
                     "Unscrupulous boxing promoters, violent bookmakers, a "
                     "Russian gangster, incompetent amateur robbers, and "
                     "supposedly Jewish jewelers fight to track down a "
                     "priceless stolen diamond",
                     "http://static.tvtropes.org/pmwiki/pub/images/Snatch.jpg",
                     "https://www.youtube.com/watch?v=Q8jbt0wBkMI")

there_will_be_blood = media.Movie("There Will Be Blood",
                                  "A story of family, religion, hatred, oil "
                                  "and madness, focusing on a turn-of-the-"
                                  "century prospector in the early days of the"
                                  " business.",
                                  "http://imgs.inkfrog.com/pix/trust2buy88/m-there_will_be_blood-07.jpg",
                                  "https://www.youtube.com/watch?v=f3THVbr4hlY")

scrooged = media.Movie("Scrooged",
                       "A selfish, cynical T.V. executive is haunted by three "
                       "spirits bearing lessons on Christmas Eve.",
                       "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSu8XJSrLHNDqjwsHntUj9z5ckOPnLUxMab_CbnJ-Fnpz_iiUbV",
                       "https://www.youtube.com/watch?v=C5s-xArZvjo")

training_day = media.Movie("Training Day",
                           "On his first day on the job as a Los Angeles "
                           "narcotics officer, a rookie cop goes on a 24-hour "
                           "training course with a rogue detective who isn't "
                           "what he appears.",
                           "http://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
                           "https://www.youtube.com/watch?v=gKTVQPOH8ZA")

basquiat = media.Movie("Basquiat",
                       "Basquiat tells the story of the meteoric rise of "
                       "youthful artist Jean-Michel Basquiat. Starting out as "
                       "a street artist, living in Thompkins Square Park in a "
                       "cardboard box, Jean-Michel is 'discovered' by Andy "
                       "Warhol's art world and becomes a star. But success has"
                       " a high price, and Basquiat pays with friendship, "
                       "love, and eventually, his life.",
                       "http://upload.wikimedia.org/wikipedia/en/3/38/Basquiatmovieposter.jpg",
                       "https://www.youtube.com/watch?v=LeTT9XYesnw")

movies = [guardians_of_the_galaxy, skyfall, snatch, there_will_be_blood,
          scrooged, training_day, basquiat, seven]
fresh_tomatoes.open_movies_page(movies)
