import media
import fresh_tomatoes

Doctor_Strange = media.Movie("Doctor_Strange(2016) ", "the war in amazing showing",
                             "http://img.goldposter.com/2016/04/Doctor-Strange_poster_goldposter_com_4.jpeg@0o_0l_800w_80q.jpg",
                             "https://www.youtube.com/watch?v=s2-1hz1juBI")

Hacksaw_ridge1=media.Movie("Hacksaw Ridge (2016) ","the war in amazing showing",
                          "http://img.goldposter.com/2016/11/hacksaw-ridge_poster_goldposter_com_9.jpg@0o_0l_800w_80q.jpg","https://www.youtube.com/watch?v=s2-1hz1juBI")

Arrival = media.Movie("Arrival(2016) ", "the war in amazing showing",
                             "http://img.goldposter.com/2016/08/Arrival_poster_goldposter_com_6.jpg", "https://www.youtube.com/watch?v=s2-1hz1juBI")


Maigrets_Dead  = media.Movie("Maigrets_Dead (2016) ", "the war in amazing showing",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BNWFkNWUyOGUtNjBmOC00ODllLThhYWYtNjkwYTI1NWQyNWJlL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjExMjk0ODk@._V1_UY1200_CR107,0,630,1200_AL_.jpg"
                             , "https://www.youtube.com/watch?v=s2-1hz1juBI")

movies=[Hacksaw_ridge1,Arrival,Doctor_Strange,Maigrets_Dead]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)