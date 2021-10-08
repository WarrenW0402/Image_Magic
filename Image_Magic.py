# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = image.getpixel((0, 0))  # grab pixel (0, 0) top-left

print(a_pixel)

