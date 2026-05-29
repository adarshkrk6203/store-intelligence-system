from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime


class StoreEvent(BaseModel):
    event_id: str
    store_id: str
    camera_id: str
    visitor_id: str
    event_type: str
    timestamp: datetime

    zone_id: Optional[str] = None
    dwell_ms: int = 0

    is_staff: bool = False
    confidence: float

    metadata: Dict = {}