import cv2
import pyautogui

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Create VideoWriter object
out = cv2.VideoWriter("recording.avi", codec, 30.0, resolution)

cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Recording", 480, 270)

while True:
    # Capture screenshot
    img = pyautogui.screenshot()

    # Convert the image into numpy array representation
    frame = np.array(img)

    # Convert the BGR image into RGB image
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the RGB image into file
    out.write(frame)

    # Display screen/frame being recorded
    cv2.imshow('Recording', frame)

    # Wait for the user to press 'q' key to stop the recording
    if cv2.waitKey(1) == ord('q'):
        break

# Close all windows after recording
out.release()
cv2.destroyAllWindows()