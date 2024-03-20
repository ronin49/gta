import cv2
import pytesseract

# Path to Tesseract executable (change this according to your installation)
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image from file
image_path = 'png.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform thresholding or other preprocessing steps if needed

# Use pytesseract to perform OCR on the grayscale image
recognized_text = pytesseract.image_to_string(gray_image)

# Print the recognized text
print("Recognized Text:")
print(recognized_text)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)  # Wait for any key press
cv2.destroyAllWindows()  # Close all OpenCV windows

