import cv2
from datetime import datetime
import pandas as pd

first_frame = None
status_list = []
times = []

df = pd.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("ERROR: Cannot open camera.")
    exit()

print("Press 'q' to quit. Move in front of the camera to trigger motion detection.")

frame_count = 0

while True:

    check, frame = video.read()
    status = 0

    if not check:
        print("ERROR: Failed to read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Set first_frame on first iteration
    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)

    thresh_frame = cv2.threshold(
        delta_frame,
        30,
        255,
        cv2.THRESH_BINARY
    )[1]

    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(
        thresh_frame.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        area = cv2.contourArea(contour)

        # Lowered threshold from 10000 to 500 — tune based on your camera/environment
        if area < 500:
            continue

        status = 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    frame_count += 1

    # Update reference frame every 30 frames to adapt to lighting changes
    if frame_count % 30 == 0:
        first_frame = gray

    status_list.append(status)

    # Debug: show current status on frame
    status_text = "Motion Detected" if status == 1 else "No Motion"
    color = (0, 0, 255) if status == 1 else (0, 255, 0)
    cv2.putText(frame, status_text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Need at least 2 entries to detect transitions
    if len(status_list) >= 2:

        # Motion started
        if status_list[-1] == 1 and status_list[-2] == 0:
            t = datetime.now()
            times.append(t)
            print(f"[MOTION STARTED] {t}")

        # Motion ended
        if status_list[-1] == 0 and status_list[-2] == 1:
            t = datetime.now()
            times.append(t)
            print(f"[MOTION ENDED]   {t}")

    cv2.imshow("Color Frame", frame)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)

    key = cv2.waitKey(1)

    if key == ord('q'):

        # If motion is still active when quitting, record end time
        if status == 1:
            times.append(datetime.now())

        break

print("\nRecorded times:", times)

# Create dataframe from paired start/end times
for i in range(0, len(times), 2):

    if i + 1 < len(times):
        start = times[i]
        end = times[i + 1]
        df.loc[len(df)] = [start, end]

# Convert columns to datetime
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

print("\nDataFrame:")
print(df)

df.to_csv("Times.csv", index=False)
print("\nSaved to Times.csv")

video.release()
cv2.destroyAllWindows()