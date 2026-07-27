# Generic AI Publishing Engine - Technology Stack

This document outlines the strictly open-source, self-hosted, and free technology stack used for building the asynchronous, on-demand AI newsletter publishing engine.

---

## 1. Core Application & Language
* **Language:** Python
* **API Framework:** FastAPI
* **Background Task Queue:** Celery
* **Cache & Message Broker:** Valkey *(The 100% open-source fork of Redis)*

## 2. AI Engine & Ingestion
* **LLM Orchestration:** LangChain & LangGraph (Core open-source Python libraries)
* **Document Parsing / Scraping:** Docling *(IBM’s open-source document conversion tool)*
* **Local LLM Runner:** Ollama
* **Open-Weights Models:** LLaMA 3 (8B) / Mistral

## 3. Database & Storage
* **Relational & Vector Database:** PostgreSQL + `pgvector` extension

## 4. Testing & Quality Control
* **Code Testing Framework:** Pytest
* **LLM Evaluation & Scoring:** Ragas or TruLens

## 5. Security & Secrets Management
* **Authentication:** OAuth2 / JWT (Built directly via FastAPI)
* **Secrets Management:** Environment variables (`.env`) / Docker Secrets / Infisical (Self-hosted)

## 6. Infrastructure & DevOps
* **Containerization:** Docker Engine
* **Container Orchestration:** Docker Compose (Single-server) / K3s (Lightweight Kubernetes for multi-server)
* **API Gateway:** Nginx Open Source
* **CI/CD Pipeline:** GitHub Actions

## 7. Observability & Monitoring
* **LLM Tracing & Telemetry:** Langfuse *(Self-hosted open-source alternative to LangSmith)*
* **System Metrics:** Prometheus + Grafana (Community Editions)