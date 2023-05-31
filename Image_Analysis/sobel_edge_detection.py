'''
In the above code, the sobel_edge_detection function takes an image and a threshold value as input. 
The threshold value determines the intensity threshold for classifying pixels as edges or non-edges.

The function first converts the input image to grayscale using cv2.cvtColor. 
Then, it applies the Sobel operator using cv2.Sobel in both the x and y directions to obtain the gradient magnitude.

The gradient magnitude is calculated as the square root of the squared x and y gradients. 
It is then normalized using cv2.normalize to the range [0, 255].

Next, a binary edge image is obtained by applying a threshold to the normalized gradient using cv2.threshold.

You can adjust the threshold value to control the sensitivity of edge detection. Smaller threshold values will result in more detected edges, 
including weaker ones, while larger threshold values will detect only stronger edges.

Feel free to modify the code and experiment with different threshold values to achieve the desired level of Sobel edge detection.
'''
import cv2
import numpy as np

def sobel_edge_detection(image, threshold):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel edge detection in the x and y directions
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the gradient magnitude
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize the gradient magnitude to the range [0, 255]
    normalized_gradient = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Apply thresholding to obtain the binary edge image
    _, edges = cv2.threshold(normalized_gradient, threshold, 255, cv2.THRESH_BINARY)

    return edges


# Load the image
image = cv2.imread('paris.jpg')

# Perform Sobel edge detection
edges = sobel_edge_detection(image, threshold=100)

# Display the original image and the detected edges
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
