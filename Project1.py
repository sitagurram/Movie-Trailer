import project1_media
import fresh_tomatoes

"""This program dispalys movies.you can play the video by clicking on poster
Files required:fresh_tomatoes.py,Project1_media.py
Software:Python"""

"""Objects of Project1_media.Python"""
toy_story = project1_media.Python(
    "Toy_story",
    "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",  # noqa
    "https://youtu.be/KYz2wyBy3kc")

twilight = project1_media.Python(
    "Twilight",
    "http://www.baltana.com/files/wallpapers-1/Twilight-Images-01560.png",
    "https://youtu.be/fFLrRlPBg0A")

avatar = project1_media.Python(
    "avatar",
    "https://upload.wikimedia.org/wikipedia/en/3/38/Avatarjakeneytiri.jpg",
    "https://youtu.be/d1_JBMrrYw8")

hungergames = project1_media.Python(
    "Hunger Games",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # noqa
    "https://youtu.be/mfmrPu43DF8")

narnia = project1_media.Python(
    "Narnia",
    "http://vignette3.wikia.nocookie.net/narnia/images/c/c5/The_chronicles_of_narnia-HD.jpg/revision/latest?cb=20131209151453",  # noqa
    "https://youtu.be/pYcGFLgJ8Uo")

huntsman_winterwar = project1_media.Python(
    "Huntsman_winterwar",
    "http://www.blackfilm.com/read/wp-content/uploads/2016/03/The-Huntsman-Winters-War-Billboard-Art.jpg",  # noqa
    "https://youtu.be/F2-_OQL9fBk")

"""creating array of objects to send to fresh_tomatoes.py"""
movies_list = [toy_story, twilight, avatar, hungergames, narnia, huntsman_winterwar]  # noqa

"""fresh_tomatoes.py will convert array of objects in to website
    displaying list of movies in the array"""
fresh_tomatoes.open_movies_page(movies_list)
