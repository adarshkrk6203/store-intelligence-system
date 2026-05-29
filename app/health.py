import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENT_FILE = os.path.join(BASE_DIR, "data", "events.jsonl")


def system_health():

    if not os.path.exists(EVENT_FILE):

        return {
            "status": "NO_EVENTS",
            "message": "No event stream found"
        }

    last_event = None

    with open(EVENT_FILE, "r", encoding="utf-8") as f:

        for line in f:

            try:
                last_event = json.loads(line)

            except:
                pass

    if last_event is None:

        return {
            "status": "EMPTY_STREAM"
        }

    last_timestamp = last_event.get("timestamp")

    return {
        "status": "HEALTHY",
        "last_event_timestamp": last_timestamp,
        "pipeline_running": True
    }