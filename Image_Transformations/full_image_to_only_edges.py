import cv2

# Load the color image
image = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, 30, 100)

# Display the edges image
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
