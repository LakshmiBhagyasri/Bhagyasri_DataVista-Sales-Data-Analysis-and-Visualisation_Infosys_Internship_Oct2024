import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Open video files
video1 = cv2.VideoCapture('C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/video1.mp4')
video2 = cv2.VideoCapture('C:/Users/bhagy/OneDrive/Pictures/Desktop/internship/video2.mp4')

# Check if the webcam and video files opened successfully
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

if not video1.isOpened():
    print("Error: Could not open video1.")
    exit()

if not video2.isOpened():
    print("Error: Could not open video2.")
    exit()

# Define codec and output video file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_webcam = cv2.VideoWriter('webcam_output.avi', fourcc, 20.0, (640, 480))
out_video1 = cv2.VideoWriter('video1_output.avi', fourcc, 20.0, (640, 480))
out_video2 = cv2.VideoWriter('video2_output.avi', fourcc, 20.0, (640, 480))

# Process webcam feed
print("Starting webcam capture...")
while True:
    ret_webcam, frame_webcam = cap.read()
    if not ret_webcam:
        print("Error: Failed to capture webcam frame.")
        break

    # Write webcam frame to output file
    out_webcam.write(frame_webcam)

    # Display the webcam frame
    cv2.imshow('Webcam', frame_webcam)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam resources
cap.release()
out_webcam.release()
cv2.destroyAllWindows()

# Process video1
print("Processing video1...")
while True:
    ret_video1, frame_video1 = video1.read()
    if not ret_video1:
        print("End of video1.")
        break

    out_video1.write(frame_video1)

    # Display video1 frame
    cv2.imshow('Video 1', frame_video1)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video1 resources
video1.release()
out_video1.release()
cv2.destroyAllWindows()

# Process video2
print("Processing video2...")
while True:
    ret_video2, frame_video2 = video2.read()
    if not ret_video2:
        print("End of video2.")
        break

    out_video2.write(frame_video2)

    # Display video2 frame
    cv2.imshow('Video 2', frame_video2)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video2 resources
video2.release()
out_video2.release()
cv2.destroyAllWindows()

print("All videos processed successfully.")
