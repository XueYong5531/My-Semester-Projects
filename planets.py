

import random
from PIL import Image
import requests
from io import BytesIO

planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]
link =["https://science.nasa.gov/wp-content/uploads/2023/11/mercury-messenger-globe-pia15162.jpg","https://media.wired.com/photos/5e59ad2b79c7100008eb6ae8/master/pass/photo_space_venus_1_S91-50688.jpg","https://images.pexels.com/photos/87651/earth-blue-planet-globe-planet-87651.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500","https://space-facts.com/wp-content/uploads/mars.jpg","https://nineplanets.org/wp-content/uploads/2019/12/Jupiter_NASAs_Hubble_Space_Telescope_June_2019jpg-300x288.jpg","https://images-assets.nasa.gov/image/PIA11141/PIA11141~large.jpg?w=1920&h=929&fit=clip&crop=faces%2Cfocalpoint","https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/uranus-1585338466.jpg","https://scx2.b-cdn.net/gfx/news/2019/30yearsagovo.jpg","https://scx2.b-cdn.net/gfx/news/2019/2-newhorizonst.jpg"]

def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

for i in range(len(planets)):
    (open_image(link[i]))



