from fastapi import FastAPI
from app.schemas import StoreEvent
from app.ingestion import ingest_event
from app.metrics import compute_metrics
from app.anomalies import detect_anomalies
from app.health import system_health
from app.funnel import compute_funnel

app = FastAPI(
    title="Store Intelligence System",
    version="1.0"
)


@app.get("/")
def root():

    return {
        "message": "Store Intelligence API Running"
    }


@app.post("/events/ingest")
def ingest(store_event: StoreEvent):

    ingest_event(store_event.model_dump(mode="json"))

    return {
        "status": "success",
        "event_type": store_event.event_type,
        "visitor_id": store_event.visitor_id
    }
    
@app.get("/metrics")
def metrics():

    return compute_metrics()

@app.get("/anomalies")
def anomalies():

    return detect_anomalies()

@app.get("/health")
def health():

    return system_health()

@app.get("/funnel")
def funnel():

    return compute_funnel()