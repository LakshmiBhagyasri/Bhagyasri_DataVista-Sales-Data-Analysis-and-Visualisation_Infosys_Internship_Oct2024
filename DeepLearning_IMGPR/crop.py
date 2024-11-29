import cv2

img = cv2.imread('C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/image1.jpeg')
cropped = img[100:200, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()