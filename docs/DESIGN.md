# DESIGN DOCUMENT

## System Goal

Build a production-style Store Intelligence System capable of processing CCTV footage into real-time retail analytics.

---

# Architecture Decisions

## Why YOLOv8?

Chosen because:

* lightweight
* fast inference
* strong community support
* easy deployment
* good enough accuracy for retail analytics

Tradeoff:
Not the most accurate model available, but offers strong speed/accuracy balance.

---

## Why ByteTrack?

Chosen because:

* robust multi-object tracking
* good performance under occlusion
* lightweight compared to DeepSORT-style approaches

Tradeoff:
Tracking IDs may occasionally switch under severe occlusion.

---

## Why JSONL Event Streaming?

Chosen because:

* simple event persistence
* replayable pipeline
* streaming-friendly architecture
* easy debugging

Tradeoff:
Not horizontally scalable like Kafka.

---

## Why FastAPI?

Chosen because:

* automatic OpenAPI documentation
* fast development
* async-ready architecture
* production-grade APIs

---

## Why Streamlit?

Chosen because:

* rapid dashboard development
* easy analytics visualization
* lightweight deployment

Tradeoff:
Not ideal for large-scale enterprise dashboards.

---

# Analytics Implemented

* Visitor counting
* Zone intelligence
* Dwell analytics
* Funnel conversion
* Anomaly detection
* Health monitoring

---

# Production Readiness Features

* Dockerized deployment
* Health APIs
* Structured event schemas
* Modular architecture
* Persistent event storage

---

# Future Scalability

Potential upgrades:

* Kafka streaming
* PostgreSQL
* Redis
* GPU inference servers
* Multi-camera fusion
* Distributed analytics pipeline
