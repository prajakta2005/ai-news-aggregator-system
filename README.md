# AI News Aggregator

An open-source AI news intelligence system that collects AI-related news from multiple public sources, processes the information using an LLM, and delivers a concise daily AI digest to subscribed users via email.

The goal of this project is not simply to aggregate news. The goal is to build an automated system that answers:

> **"What actually happened in AI today, and why does it matter?"**

## Project Vision

The system will collect news from multiple sources such as RSS feeds and public AI/technology publications.

The collected information will then be processed, cleaned, deduplicated, and analyzed using an LLM.

Every day, at a configured time, the system will generate a concise AI news digest and send it to all subscribed users.

The intended user experience is:

```text
User visits website
        ↓
Enters email
        ↓
Subscribes
        ↓
System collects AI news every day
        ↓
AI analyzes the day's developments
        ↓
Daily digest is generated
        ↓
User receives the digest by email
```

## System Overview

```text
                    ┌─────────────────────┐
                    │       SOURCES       │
                    │                     │
                    │ RSS Feeds           │
                    │ AI Blogs            │
                    │ Tech Publications   │
                    │ Public Sources      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   NEWS INGESTION    │
                    │                     │
                    │ Fetch               │
                    │ Parse               │
                    │ Normalize           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PROCESSING      │
                    │                     │
                    │ Validate            │
                    │ Filter              │
                    │ Deduplicate         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    AI PROCESSING    │
                    │                     │
                    │ Summarize           │
                    │ Extract key points  │
                    │ Identify importance │
                    │ Generate synthesis  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    DAILY DIGEST     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    EMAIL DELIVERY   │
                    └──────────┬──────────┘
                               │
                               ▼
                           Subscriber
```

## Current Development Phase

The project is being developed incrementally.

### Phase 01 — News Ingestion & Storage

The first phase focuses on building a reliable news collection pipeline.

```text
RSS Sources
    ↓
Fetch
    ↓
Parse
    ↓
Normalize
    ↓
Validate
    ↓
Deduplicate
    ↓
PostgreSQL
```

Phase 01 does **not** focus on LLM processing or email delivery yet.

The purpose is to establish a reliable foundation for the later AI pipeline.

### Phase 02 — AI Intelligence

The second phase will introduce the LLM layer.

```text
Stored Articles
      ↓
Article Selection
      ↓
LLM Processing
      ↓
Summarization
      ↓
Key Points
      ↓
Importance / Relevance
      ↓
Daily Digest
```

The primary LLM will initially use the Gemini API Free Tier.

The architecture will keep the LLM provider replaceable so that other free or local models can be used when necessary.

### Phase 03 — Automation & Delivery

The final phase will connect the complete system.

```text
Scheduler
    ↓
Collect News
    ↓
Process News
    ↓
Generate AI Digest
    ↓
Find Subscribers
    ↓
Send Email
```

A lightweight web interface will allow users to subscribe with their email address.

## Technology Stack

| Component        | Technology            |
| ---------------- | --------------------- |
| Language         | Python                |
| Backend          | FastAPI               |
| Database         | PostgreSQL            |
| ORM              | SQLAlchemy            |
| Validation       | Pydantic              |
| News Collection  | RSS / Public Sources  |
| RSS Parser       | feedparser            |
| HTTP Client      | httpx                 |
| LLM              | Gemini API Free Tier  |
| LLM Fallback     | Ollama / Local Models |
| Frontend         | Next.js + TypeScript  |
| Styling          | Tailwind CSS          |
| Scheduling       | APScheduler           |
| Testing          | Pytest                |
| Containerization | Docker                |
| CI/CD            | GitHub Actions        |
| Version Control  | Git + GitHub          |

## Cost Constraint

This project is being developed with a **₹0 development budget** as a core constraint.

We will prioritize:

* Open-source software
* Public RSS feeds
* Free APIs and free tiers
* Local/open-weight models where appropriate
* Free development and deployment options
* Self-hosted components when practical

The system should not depend on a paid API to function during development.

The LLM layer will initially use the Gemini API Free Tier, with Ollama/local models available as a fallback during development.

Free-tier limits and service availability may change over time, so provider-specific dependencies will be isolated behind application interfaces wherever practical.

## Design Principles

### 1. Understand Before Implementing

Every major component will be understood before it is implemented.

### 2. Simple Before Complex

We will not introduce infrastructure or frameworks unless they solve an actual problem.

### 3. AI Is a Component, Not the Entire Application

The project is an automated data and intelligence pipeline in which an LLM is one component.

### 4. Provider Independence

The application should not be tightly coupled to a single LLM provider.

### 5. Reliability Before Intelligence

A reliable news ingestion pipeline must exist before sophisticated AI processing is introduced.

### 6. Test as We Build

Testing will be introduced alongside features rather than at the end of development.

### 7. Learn Through Implementation

Every feature should answer two questions:

* Why does this component exist?
* What engineering concept does implementing it teach?

## Project Structure

The project will be developed incrementally.

The initial structure is intentionally small:

```text
ai-news-aggregator/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│
├── scripts/
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

As the project develops, application responsibilities will be separated into areas such as:

```text
app/
├── api/
├── core/
├── db/
├── ingestion/
├── processing/
├── ai/
├── digest/
└── email/
```

These modules will be introduced when their functionality is implemented.

## Development Workflow

Development will follow:

```text
Understand
    ↓
Design
    ↓
Implement
    ↓
Test
    ↓
Document
    ↓
Commit
```

Git branches will be used for major phases and features.

Example:

```text
main
 │
 └── phase-01-foundation
       │
       ├── feature/rss-ingestion
       ├── feature/database
       └── feature/deduplication
```

## Future Features

The initial version will focus on the core daily digest pipeline.

Potential future improvements include:

* Personalized news categories
* Topic preferences
* AI news search
* Digest archive
* "Ask about today's AI news"
* Related-story clustering
* Source credibility signals
* Article relevance scoring
* User preferences
* Unsubscribe management
* Admin dashboard
* Observability and monitoring
* Automated evaluation of AI-generated summaries

These features will only be introduced after the core pipeline is reliable.

## Project Status

**Current phase:** Phase 01 — News Ingestion & Storage

**Status:** Under active development

The project is being rebuilt from the ground up as a learning-focused implementation.

## License

This project is open source. License details will be finalized as the project develops.
