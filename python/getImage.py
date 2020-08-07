#pip install pillow
from urllib import request
from io import BytesIO
from PIL import Image

image_url = "https://i.pinimg.com/originals/84/bc/ee/84bceead3a74653f60d4f5ff106bb7c6.jpg"

# request.urlopen()
res = request.urlopen(image_url).read()

# Image open
img = Image.open(BytesIO(res))

print(img)