from app.metrics import load_events


def compute_funnel():

    events = load_events()

    entered_store = set()
    visited_billing = set()

    for event in events:

        visitor_id = event.get("visitor_id")
        event_type = event.get("event_type")
        zone_id = event.get("zone_id")

        # Store entries
        if event_type == "ENTRY":
            entered_store.add(visitor_id)

        # Billing visitors
        if (
            event_type == "ZONE_ENTER"
            and zone_id == "BILLING"
        ):
            visited_billing.add(visitor_id)

    total_entries = len(entered_store)
    billing_visitors = len(visited_billing)

    conversion_rate = 0

    if total_entries > 0:

        conversion_rate = round(
            (billing_visitors / total_entries) * 100,
            2
        )

    return {

        "store_entries": total_entries,

        "billing_visitors": billing_visitors,

        "conversion_rate_percent": conversion_rate
    }