# Master System & Project Context

**INSTRUCTION TO AI:** Parse this document entirely before providing any responses. This document serves as the absolute ground truth for the current project context, technical architecture, and user preferences.

---

## 1. Communication & Output Directives
* **Response Style:** Think more, talk less. Provide clear, crisp, and concise answers.
* **Terminology:** Use layman terms where possible. Absolutely no fluff and no unnecessary jargon.
* **Format:** Use structured bullet points, code blocks, and direct answers.

## 2. Professional Context
* **Domain:** Quality Assurance Automation & Generative AI Data Science.
* **Focus Areas:** Advanced machine learning architectures, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) systems, and model fine-tuning workflows.

## 3. Technical Stack & Infrastructure
* **Core Language:** Python
* **API & Backend:** FastAPI
* **AI/LLM Frameworks:** LangChain, LangGraph
* **Containerization:** Docker
* **Vector Store/Database:** [Placeholder: e.g., FAISS, ChromaDB, Pinecone]
* **Embedding Model:** [Placeholder: e.g., text-embedding-004]
* **Primary LLM:** [Placeholder: e.g., Gemini 1.5 Pro, GPT-4o, Claude 3.5 Sonnet]

## 4. Architectural Blueprint
### 4.1. Data Ingestion & Processing
* **Sources:** [Detail where the data originates (e.g., S3 buckets, internal APIs, uploaded PDFs)]
* **Parsing & Chunking:** [Specify the chunking strategy, overlap size, and parsing libraries]
* **Embedding Pipeline:** [Detail how text is converted to vectors and stored]

### 4.2. Execution Flow (LangGraph / LangChain)
* **Routing Logic:** [Explain how user queries are classified and routed]
* **Retrieval Strategy:** [e.g., Semantic search, hybrid search with BM25, query reformulation]
* **Generation & Synthesis:** [Detail the prompt templates and synthesis strategy]
* **Fallback Mechanisms:** [What happens when retrieval fails or confidence is low?]

### 4.3. API & Integration
* **Endpoints:** [List core FastAPI routes, e.g., `/api/v1/chat`, `/api/v1/ingest`]
* **Authentication:** [Specify auth mechanisms]

## 5. Functional & Non-Functional Requirements
### Functional
* **1.** [Detailed functional requirement 1]
* **2.** [Detailed functional requirement 2]
* **3.** [Detailed functional requirement 3]

### Non-Functional
* **Latency:** [Target response time for inference]
* **Scalability:** [Expected concurrent users/requests]
* **Quality Assurance:** [Evaluation metrics for LLM outputs (e.g., RAGAS, precision/recall)]

## 6. Current Project State
* **Completed Milestones:** 
  * [Detail what is already built and working perfectly]
* **Active Development:** 
  * [Detail what is currently being coded]
* **Known Issues / Bugs:**
  * [Detail any specific errors, traceback logs, or logical flaws currently present]

## 7. Immediate Task for this Session
* **Objective:** [Define exactly what needs to be solved in the current chat window]
* **Expected Output:** [e.g., "Refactored LangGraph node code", "A Dockerfile for the FastAPI app", "Debugging a specific exception"]