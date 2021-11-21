import PIL
from PIL import Image
from tkinter.filedialog import *

# Ask for filepath
file_path = askopenfilename()

# Set image to pillow library
img = PIL.Image.open(file_path)

# Set the height and width of image
my_height, my_width = img.size

# Compress our image
img = img.resize((my_height, my_width), PIL.Image.ANTIALIAS)

# Save location
save_path = asksaveasfilename()

# Save our image
img.save(save_path+"_compressed.JPG")