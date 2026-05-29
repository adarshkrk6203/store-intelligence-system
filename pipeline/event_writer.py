import json


EVENT_FILE = "data/events.jsonl"


def save_event(event):

    with open(EVENT_FILE, "a") as f:

        json.dump(event, f)

        f.write("\n")