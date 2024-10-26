import cv2
import os

# Paths to the images (use absolute paths if needed)
img_path = 'C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/image1.jpeg'
template_path = 'template.png'

# Check if the image files exist
if not os.path.exists(img_path) or not os.path.exists(template_path):
    print(f"Error: One or both files not found:\nImage: {img_path}\nTemplate: {template_path}")
    exit()

# Load the main image and the template
img = cv2.imread(img_path)
template = cv2.imread(template_path, 0)  # Load template in grayscale

# Check if the images were loaded properly
if img is None:
    print(f"Error: Could not load image '{img_path}'")
    exit()
if template is None:
    print(f"Error: Could not load template '{template_path}'")
    exit()

# Convert the main image to grayscale (to match the template's depth)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Get the best match location
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
h, w = template.shape[:2]
bottom_right = (top_left[0] + w, top_left[1] + h)

# Draw a rectangle around the detected template
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

# Display the result
cv2.imshow('Detected Template', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
