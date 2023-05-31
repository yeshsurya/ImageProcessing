import cv2
import numpy as np

def impulse_noise_reduction(image, kernel_size, threshold):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median filtering
    filtered = cv2.medianBlur(gray, kernel_size)

    # Find pixels affected by impulse noise
    diff = cv2.absdiff(gray, filtered)
    _, mask = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Replace noisy pixels with median filtered values
    result = np.where(mask, filtered, gray)

    return result


# Load the image
image = cv2.imread('paris.jpg')

# Apply impulse noise reduction
filtered_image = impulse_noise_reduction(image, kernel_size=3, threshold=30)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
