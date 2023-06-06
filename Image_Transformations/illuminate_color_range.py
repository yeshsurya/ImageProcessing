import cv2
import numpy as np

# Load the image
image = cv2.imread('input_image.jpg')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the color range you want to illuminate
lower_range = np.array([hue_min, saturation_min, value_min], dtype=np.uint8)
upper_range = np.array([hue_max, saturation_max, value_max], dtype=np.uint8)

# Create a binary mask based on the color range
mask = cv2.inRange(hsv, lower_range, upper_range)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
