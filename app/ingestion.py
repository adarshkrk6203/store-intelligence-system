import json
import os
from fastapi.encoders import jsonable_encoder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVENT_FILE = os.path.join(BASE_DIR, "data", "events.jsonl")


def ingest_event(event):
    os.makedirs(os.path.dirname(EVENT_FILE), exist_ok=True)

    with open(EVENT_FILE, "a", encoding="utf-8") as f:
        json.dump(jsonable_encoder(event), f)
        f.write("\n")