#the file in which we are defining a bunch of movie instances

import fresh_tomatoes
import media

father_goose = media.Movie("Father Goose",
                           "Set during WWII, a high-functioning alcoholic coastwatcher attempts to unravel a military "
                           "code to uncover a stash of booze.",
                           "http://www.impawards.com/1964/posters/father_goose_ver2_xlg.jpg",
                           "https://youtu.be/C-F3vSrJIUQ")

toy_story = media.Movie("Toy Story",
                        "A heartfelt story of sentient toys and their owners who are moving out of the uncanny value.",
                        "http://www.cultjer.com/img/ug_photo/2015_09/32772420150915154419.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "James Cameron's long-awaited and visually stunning Titanic sequel.",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_life_aquatic_with_steve_zissou = media.Movie("The Life Aquatic with Steve Zissou",
                               "A bond company stooge accompanies a washed-up oceanographer on an expedition and "
                               "finds his courage.",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzODYzNzg2MF5BMl5BanBnXkFtZTcw"
                               "MTkzOTQzMw@@._V1_SY1000_CR0,0,684,1000_AL_.jpg",
                               "https://www.youtube.com/watch?v=XVt9g-uQOx0")

guardians_of_the_galaxy_vol_2 = media.Movie("Guardians of the Galaxy Vol. 2",
                                             "A 70s music video set to a super fun sci-fi plot.",
                                             "https://media0dk-a.akamaihd.net/56/44/9309ee7890499a5b4d7d825f02dbe80e"
                                             ".jpg",
                                             "https://www.youtube.com/watch?v=2cv2ueYnKjg")

monsters_inc = media.Movie("Monsters, Inc.",
                           "Monsters undergo complete economic reform. Those who can't adapt are left behind.",
                           "https://o.aolcdn.com/images/dims?resize=270%2C400&quality=70&image_uri=http%3A%2F%2Faolx."
                           "tmsimg.com%2Fmovieposters%2Fv7%2FAllPhotos%2F27462%2Fp27462_d_v7_aa.jpg%3Fw%3D270&client="
                           "cbc79c14efcebee57402&signature=608e2fd710a86cfa02f176ff3e8b920e13505866",
                           "https://www.youtube.com/watch?v=cvOQeozL4S0")

movies = [father_goose, toy_story, avatar, the_life_aquatic_with_steve_zissou, guardians_of_the_galaxy_vol_2,
          monsters_inc]
fresh_tomatoes.open_movies_page(movies)

# Things I Learned:
# print toy_story.storyline
# the_life_aquatic.show_trailer()
# print (media.Movie.VALID_RATINGS)
# print media.Movie.__doc__
# print media.Movie.__name__ #prints the name of the class
# print media.Movie.__module__#prints the name of the module in which this class was defined