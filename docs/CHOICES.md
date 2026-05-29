# ENGINEERING CHOICES & TRADEOFFS

## Simplicity Over Overengineering

The hidden evaluation dataset encouraged building a generalized and robust pipeline rather than overfitting to specific footage.

The system prioritizes:

* modularity
* reliability
* explainability
* deployment simplicity

over extremely complex CV architectures.

---

# Tracking Strategy

Instead of implementing heavy Re-ID models, the system uses:

* ByteTrack persistence
* trajectory continuity
* temporal consistency

Reason:
Retail analytics does not require perfect biometric identification.

---

# Event-Driven Architecture

The pipeline converts raw video into structured business events.

Advantages:

* decoupled services
* replayability
* analytics flexibility
* scalable architecture

---

# Why Rule-Based Analytics?

Many retail analytics problems:

* overcrowding
* zone traffic
* dwell analytics

can be solved reliably with lightweight rule systems.

This improves:

* explainability
* robustness
* debugging simplicity

---

# Production Considerations

The project includes:

* health monitoring
* Docker deployment
* modular APIs
* dashboard visualization

to reflect production engineering practices.

---

# Known Limitations

* Single-camera assumptions
* Possible ID switching
* Polygon zones manually configured
* JSONL not horizontally scalable

---

# Future Improvements

* Multi-camera tracking
* Learned anomaly detection
* Kafka streaming
* Distributed event processing
* GPU acceleration
