import numpy as np
from skimage import color, io

# Load RGB image
rgb_image = io.imread('input_image.jpg')

# Convert RGB image to CIELAB color space
lab_image = color.rgb2lab(rgb_image)

# Save CIELAB image
io.imsave('output_image.jpg', lab_image)
