import time

from ultralytics import YOLO
import cv2

from events import create_event
from zones import get_zone
from event_writer import save_event

# Load YOLO
model = YOLO("yolov8n.pt")

# Video path
video_path = "videos/sample.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

# Seen visitors
seen_ids = set()

# Store visitor zones
visitor_zones = {}
zone_entry_times = {}

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    # Run tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        classes=[0],
        verbose=False
    )

    boxes = results[0].boxes

    if boxes.id is not None:

        track_ids = boxes.id.int().cpu().tolist()
        confidences = boxes.conf.cpu().tolist()
        xyxy_boxes = boxes.xyxy.cpu().tolist()

        for track_id, conf, box in zip(track_ids, confidences, xyxy_boxes):

            visitor_id = f"VIS_{track_id}"

            x1, y1, x2, y2 = box

            # Center point
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Get current zone
            current_zone = get_zone(center_x, center_y)

            # First time visitor seen
            if visitor_id not in seen_ids:

                seen_ids.add(visitor_id)

                entry_event = create_event(
                    store_id="STORE_001",
                    camera_id="CAM_001",
                    visitor_id=visitor_id,
                    event_type="ENTRY",
                    confidence=float(conf)
                )

                save_event(entry_event)

                print("\nENTRY EVENT:")
                print(entry_event)

            # Zone tracking
            previous_zone = visitor_zones.get(visitor_id)

                        # Zone changed
                        # Zone changed
            if current_zone != previous_zone:

                current_time = time.time()

                # Exit old zone
                if previous_zone is not None:

                    enter_time = zone_entry_times.get(visitor_id)

                    dwell_ms = 0

                    if enter_time is not None:

                        dwell_ms = int(
                            (current_time - enter_time) * 1000
                        )

                    exit_event = create_event(
                        store_id="STORE_001",
                        camera_id="CAM_001",
                        visitor_id=visitor_id,
                        event_type="ZONE_EXIT",
                        confidence=float(conf),
                        zone_id=previous_zone,
                        dwell_ms=dwell_ms
                    )

                    save_event(exit_event)

                    print("\nZONE EXIT:")
                    print(exit_event)

                # Enter new zone
                if current_zone is not None:

                    zone_entry_times[visitor_id] = current_time

                    enter_event = create_event(
                        store_id="STORE_001",
                        camera_id="CAM_001",
                        visitor_id=visitor_id,
                        event_type="ZONE_ENTER",
                        confidence=float(conf),
                        zone_id=current_zone
                    )

                    save_event(enter_event)

                    print("\nZONE ENTER:")
                    print(enter_event)

                # Update visitor zone
                visitor_zones[visitor_id] = current_zone

    # Draw tracking
    annotated_frame = results[0].plot()

    # Draw zones visually
    cv2.rectangle(annotated_frame, (0, 0), (250, 720), (0, 255, 0), 2)
    cv2.putText(
        annotated_frame,
        "ENTRY",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.rectangle(annotated_frame, (900, 0), (1280, 720), (255, 0, 0), 2)
    cv2.putText(
        annotated_frame,
        "BILLING",
        (950, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Store Intelligence", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("\nProcessing Complete")