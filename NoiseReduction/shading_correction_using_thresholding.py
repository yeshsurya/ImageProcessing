import cv2

def shading_correction(image, block_size, constant):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding for shading correction
    corrected = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)

    return corrected


# Load the image
image = cv2.imread('image.jpg')

# Apply shading correction
shading_corrected = shading_correction(image, block_size=11, constant=2)

# Display the original and shading-corrected images
cv2.imshow('Original Image', image)
cv2.imshow('Shading Corrected', shading_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
