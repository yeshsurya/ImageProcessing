import cv2

def edge_detection(image, threshold1, threshold2):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, threshold1, threshold2)

    return edges


# Load the image
image = cv2.imread('paris.jpg')

# Perform edge detection
edges = edge_detection(image, threshold1=100, threshold2=200)

# Display the original image and the detected edges
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
