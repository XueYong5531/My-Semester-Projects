#Xue Yong Li
#2/24/25
#Random Image Recommender
#Start by importing the necessary libraries
#Init
import random
import time
from PIL import Image
import requests
from io import BytesIO
locations = ["https://www.andrewshoemaker.com/images/xl/burning-secret-maui-secret-beach-sunset.jpg", "https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/02/a0002487/img/basic/a0002487_main.jpg", "https://www.howardcc.edu/media/howardcc/programs-courses/study-abroad/images/Blog-Rome-300273-2022-Rome-shutterstock_1417390817-Hybris.jpg", "https://www.thetopvillas.com/blog/wp-content/uploads/2022/10/bali.jpg", "https://www.responsiblevacation.com/imagesclient/L_184831.jpg"]
#Functions
#Define a function called open_image with a url parameter for the image address

def recommender():
    print("Welcome to Random Vacation Recommender")
    print("Would you like a recommendation for a vacation spot?")
    while True:
        decision = int(input("Yes (1) || No (2)"))
        if decision == 1:
            print("Recommending...")
            time.sleep(1)
            location = random.choice(locations)
            open_image(location)
            if location == "https://www.andrewshoemaker.com/images/xl/burning-secret-maui-secret-beach-sunset.jpg":
                print("I recommend traveling to Hawaii because of its spectacular scenary, diverse culture, rich history, and a great place to relax!")
            elif location == "https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/02/a0002487/img/basic/a0002487_main.jpg":
                print("I recommend traveling to Japan because of its combination of a rich history, modern convienances, cleanliness, food, and tourist attractions make a great spot!")
            elif location == "https://www.howardcc.edu/media/howardcc/programs-courses/study-abroad/images/Blog-Rome-300273-2022-Rome-shutterstock_1417390817-Hybris.jpg":
                print("I recommend traveling to Rome because of its rich history of art, architecture, and beauty of food and its culture make somewhere you cant miss!")
            elif location == "https://www.thetopvillas.com/blog/wp-content/uploads/2022/10/bali.jpg":
                print("I recommend traveling to Thailand for its tropical atmostphere, lush enviroment, great cuisine, and natural beauty makes it a bucket-list location")
            elif location == "https://www.responsiblevacation.com/imagesclient/L_184831.jpg":
                print("I recommend traveling to Lapland during the winter time for its magical winter snow and northern light sightings that make a great cozy atmosphere!")
        else:
            break


def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

#Main
#Call your function with an image URL
recommender()


#DO NOT FORGET TO CITE YOUR SOURCE
#The adorable face of a dog. Image source: The Dog API. 2009. Accessed via https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg CC BY-NC 2.0.

#Citations:
#Hawaii - https://www.andrewshoemaker.com/images/xl/burning-secret-maui-secret-beach-sunset.jpg (andrewshoemaker.com | Andrew Shoemaker | https://www.andrewshoemaker.com/gallery/photographers-guide-to-hawaiian-islands/ | "A Photographer’s Guide to the Best Photography Spots in Hawaii" | May 31, 2024 |)
#Japan - https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/02/a0002487/img/basic/a0002487_main.jpg (livejapan.com | Lucio MAaurizi | https://livejapan.com/en/article-a0002487/ | "Japan Travel Tips: 9 Things I Wish I'd Known Before Going to Japan" | January 6, 2023|)
#Rome - https://www.howardcc.edu/media/howardcc/programs-courses/study-abroad/images/Blog-Rome-300273-2022-Rome-shutterstock_1417390817-Hybris.jpg (howardcc.edu | Unknown Author | https://www.howardcc.edu/programs-courses/academics/office-of-international-education/programs/all-roads-lead-to-rome-exploring-ancient-italy/ | "All Roads Lead to Rome: Exploring Ancient Italy" | Unknown Date)
#Thailand - https://www.thetopvillas.com/blog/wp-content/uploads/2022/10/bali.jpg (thetopvillas.com | Tamara del Renzio | https://www.thetopvillas.com/blog/travel-guides/amazing-vacation-destinations/#koh | "Amazing destinations for vacations in 2024" | Unknown Date|)
#Lapland - https://www.responsiblevacation.com/imagesclient/L_184831.jpg (responsiblevacation.com | Unknwon Author | https://www.responsiblevacation.com/vacation/16919/lapland-vacation-husky-safari--log-cottage | "Lapland vacation, husky safari & log cottage" | Unknown Date|)


