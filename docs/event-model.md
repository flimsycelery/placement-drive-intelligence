# Event Model

## Overview

The Campus Placement Intelligence Platform follows an event-driven architecture.

Rather than directly updating business tables, the platform records every business activity as an immutable event.

This approach preserves historical information, enables auditing, and supports incremental processing.

---

## Event Structure

Each event contains the following information:

| Field | Description |
|--------|-------------|
| Event_ID | Unique event identifier |
| Event_Type | Type of business event |
| Event_Timestamp | Date and time when the event occurred |
| Source_System | System that generated the event |
| Entity_ID | Business entity associated with the event |
| Payload | Event-specific information |

---

## Event Types

### Company Events

- Company Created
- Placement Drive Created
- Placement Drive Updated
- Deadline Extended

---

### Student Events

- Student Created
- Student Profile Updated
- Student Skills Updated
- Student CGPA Updated
- Student Backlog Status Updated
- Student Registered
- Student Registration Withdrawn

---

### Interview Events

- Interview Scheduled
- Interview Rescheduled
- Interview Completed

---

### Offer Events

- Offer Released
- Offer Accepted
- Offer Rejected

---

## Why Event-Driven?

Recording business activities as events provides several advantages:

- Preserves complete historical records
- Enables auditability
- Supports incremental data processing
- Simplifies downstream analytics
- Allows replaying historical events if needed

---

## Relationship with Medallion Architecture

### Bronze

Stores every raw event exactly as generated.

### Silver

Validates, cleans, and standardizes event data.

### Gold

Transforms validated events into analytical datasets for reporting and dashboards.