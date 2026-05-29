import uuid
from datetime import datetime


def create_event(
    store_id,
    camera_id,
    visitor_id,
    event_type,
    confidence=1.0,
    zone_id=None,
    dwell_ms=0,
    is_staff=False,
    metadata=None
):

    if metadata is None:
        metadata = {}

    event = {
        "event_id": str(uuid.uuid4()),
        "store_id": store_id,
        "camera_id": camera_id,
        "visitor_id": visitor_id,
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": zone_id,
        "dwell_ms": dwell_ms,
        "is_staff": is_staff,
        "confidence": confidence,
        "metadata": metadata
    }

    return event