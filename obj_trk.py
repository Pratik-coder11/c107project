import cv2
import time 
import math

cap = cv2.VideoCapture('footvolleyball.mp4')

tracker = cv2.TrackerCSRT_create()

ret, frame = cap.read()

bbox = cv2.selectROI(frame, False)

tracker.init(frame, bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def goal_track(img, bbox):
    pass




while True:
    # Read the current frame
    check, img = cap.read()

    # Update the tracker
    success, bbox = tracker.update(img)

    if success:
        # If tracking is successful, draw the bounding box
        drawBox(img, bbox)
        goal_track(img, bbox)
    else:
        # If tracking is lost, display "LOST" on the screen
        cv2.putText(img, "LOST", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Show the image
    cv2.imshow('Tracking', img)

    # Break the loop with the 'q' key
    key = cv2.waitKey(1)
    if key == ord('q'):
        print("Closing")
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
