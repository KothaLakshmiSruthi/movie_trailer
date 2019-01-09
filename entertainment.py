import media
import fresh_tomatoes
remo=media.Movies("REMO(Telugu)","director:Bakkiyaraj Kannan","ratings:4.0",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5c2xqc2DyDfRuiLVDvjHoHMYkn9AJmd7OXDvVnnnukDh2CO08Zw",
                      "https://youtu.be/DZJ8NMBZW-E")

robo=media.Movies("ROBO-2.O(Telugu)","director:S.Shankar","ratings:4.5",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuVzOOHp4srCaAAIcbroeiRpb-g1bgb5JLxRBYoQ2GEw86Q7IR3Q",
                      "https://www.youtube.com/watch?v=_qOl_7qfPOM")

sarkar=media.Movies("SARKAR(Telugu)","director:A.R. Murugadoss","ratings:3.5",
                  "https://pbs.twimg.com/media/DqBl18rVsAAU9oL.jpg",
                  "https://youtu.be/JsE4qInfmZ0")

ongolugitta=media.Movies("ONGOLU GITTA(Telugu)","director:Bhaskar","ratings:4.5",
                         "https://www.filmibeat.com/ph-big/2013/01/ongole-gitta_13596075686.jpg",
                         "https://youtu.be/43wzetpFKiY")

awe=media.Movies("AWE(Telugu)","director:Prashanth Varma","ratings:4.0 ",
                 "https://www.c65.in/wp-content/uploads/c65gallery/awe-movie-releasing-today-posters/awe-movie-releasing-today-posters-0eb6205.jpg",
                 "https://youtu.be/xOEscQChX7M")


gentleman=media.Movies("GENTLE MAN(Telugu)","director:Mohan Krishna Indraganti","ratings:4.0",
                       "https://i.pinimg.com/originals/a5/35/a8/a535a866730e16d0421a9b03db2bf0a0.jpg",
                       "https://youtu.be/MgmowJ5r-es")

movies=[remo,robo,sarkar,ongolugitta,awe,gentleman]
fresh_tomatoes.open_movies_page(movies)
                
