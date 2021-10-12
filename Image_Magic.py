# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

# Load the image (pumpkin)
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = output_image.getpixel((0, 0))  # grab pixel (0, 0) top-left

print(a_pixel)

# Iterate over EVERY PIXEL
# Get dimensions (size) of the image
image_width = output_image.width
image_height = output_image.height

# Top to bottom
for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        pixel = output_image.getpixel((x, y))

        #print(f"\nPixel Location: {x}, {y}")
        # Print pixel values
        #print(f"red: {pixel[0]}")
        #print(f"green: {pixel[1]}")
        #print(f"blue: {pixel[2]}")

        red, green, blue = pixel

        average = int(sum(pixel)/len(pixel))

        grey_pixel = (average,average,average)
        output_image.putpixel((x, y), grey_pixel)

output_image.save('greyscale.jpg')