import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENT_FILE = os.path.join(BASE_DIR, "data", "events.jsonl")


def load_events():
    events = []

    if not os.path.exists(EVENT_FILE):
        return events

    with open(EVENT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass

    return events


def compute_metrics():
    events = load_events()

    unique_visitors = set()
    total_entries = 0
    zone_counts = {}
    total_dwell_ms = 0
    dwell_events = 0

    for event in events:
        visitor_id = event.get("visitor_id")
        event_type = event.get("event_type")
        zone_id = event.get("zone_id")

        if visitor_id:
            unique_visitors.add(visitor_id)

        if event_type == "ENTRY":
            total_entries += 1

        if event_type == "ZONE_ENTER":
            zone_counts[zone_id] = zone_counts.get(zone_id, 0) + 1

        if event_type == "ZONE_EXIT":
            dwell_ms = event.get("dwell_ms", 0) or 0
            if dwell_ms > 0:
                total_dwell_ms += dwell_ms
                dwell_events += 1

    average_dwell_seconds = round((total_dwell_ms / dwell_events) / 1000, 2) if dwell_events else 0

    return {
        "total_events": len(events),
        "total_entries": total_entries,
        "unique_visitors": len(unique_visitors),
        "zone_counts": zone_counts,
        "average_dwell_seconds": average_dwell_seconds,
    }