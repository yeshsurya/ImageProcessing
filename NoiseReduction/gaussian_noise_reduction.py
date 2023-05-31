import cv2

def gaussian_noise_reduction(image, kernel_size):
    # Apply Gaussian filtering
    filtered = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    return filtered


# Load the image
image = cv2.imread('paris.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian noise reduction
filtered_image = gaussian_noise_reduction(gray, kernel_size=3)

# Display the original and filtered images
cv2.imshow('Original Image', gray)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
