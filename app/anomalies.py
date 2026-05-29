from app.metrics import load_events


def detect_anomalies():

    events = load_events()

    anomalies = []

    zone_counts = {}

    # Count zone traffic
    for event in events:

        if event.get("event_type") == "ZONE_ENTER":

            zone = event.get("zone_id")

            if zone not in zone_counts:
                zone_counts[zone] = 0

            zone_counts[zone] += 1

    # Detect overcrowding
    for zone, count in zone_counts.items():

        if count > 50:

            anomalies.append({
                "type": "OVERCROWDING",
                "zone": zone,
                "count": count
            })

    # Detect low traffic
    for zone, count in zone_counts.items():

        if count < 2:

            anomalies.append({
                "type": "LOW_TRAFFIC",
                "zone": zone,
                "count": count
            })

    return anomalies