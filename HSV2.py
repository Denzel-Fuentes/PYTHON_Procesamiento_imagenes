import cv2
import numpy as np
 
def filter_pink(frame):
  hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  lower_rosado = np.array([150, 110, 110], np.uint8)  
  upper_blue = np.array([180, 250, 250], np.uint8)  
  pink_mask = cv2.inRange(hsv_frame, lower_rosado, upper_blue)
  filtered_frame = cv2.bitwise_and(frame, frame, mask=pink_mask)
  return filtered_frame
 
cap = cv2.VideoCapture(0)
 
if not cap.isOpened():
  print("Error opening camera")
  exit()
 
while True:
  ret, frame = cap.read()
 
  if not ret:
    print("Error reading frame")
    break
 
  # Filter the pink color from the frame
  filtered_frame = filter_pink(frame)  # Call the defined function
 
  # Display the original and filtered frames side-by-side
  cv2.imshow("Original Frame", frame)
  cv2.imshow("Filtered Frame", filtered_frame)
 
  # Exit on 'q' key press
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
 
# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()