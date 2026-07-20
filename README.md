# AI News Aggregator

An AI-powered news aggregation system that collects and curates the latest developments in artificial intelligence — built entirely with **free, open-source tools**.

## Stack (100% free)

| Component | Tool | Cost |
|-----------|------|------|
| Database | PostgreSQL in Docker | Free |
| LLM | Ollama (Llama 3.2, local) | Free |
| YouTube feeds | RSS (public feeds) | Free |
| Blog scraping | httpx + trafilatura (open source) | Free |
| Email | [Resend](https://resend.com) free tier | 3,000 emails/month |

> **Note on OpenAI:** The OpenAI API is pay-per-use — there is no free production tier. This project uses **Ollama** instead so viewers can follow along without paying for anything.

## What it does

1. **Collects** videos from YouTube channels via RSS feeds
2. **Scrapes** full blog post content from AI organizations (OpenAI, Anthropic, etc.)
3. **Stores** everything in PostgreSQL (Docker container)
4. **Summarizes** with a local LLM using prompts in the `agent/` folder
5. **Emails** a curated daily digest via Resend

## Project structure

```
ai-news-aggregator/
├── agent/
│   ├── prompts/              # System & user prompts (edit these!)
│   │   ├── digest_system.txt
│   │   └── digest_user.txt
│   └── digest_agent.py       # LLM agent that loads prompts & calls Ollama
├── app/
│   ├── collectors/           # RSS feeds, blog scrapers, full-page extraction
│   ├── models/               # SQLAlchemy data models
│   ├── notifications/        # Resend email delivery
│   └── pipeline/             # Daily orchestration
├── docker-compose.yml        # PostgreSQL + Ollama containers
├── main.py
└── pyproject.toml
```

## Prerequisites

- Python 3.12+
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Free [Resend](https://resend.com) account (for email)

## Setup

### 1. Install Python dependencies

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
```

### 2. Start Docker services

```bash
docker compose up -d
```

This starts:
- **PostgreSQL** on port `5432`
- **Ollama** on port `11434`

### 3. Pull the LLM model (one-time)

```bash
docker compose exec ollama ollama pull llama3.2
```

This downloads Llama 3.2 (~2 GB). It runs locally — no API key needed.

### 4. Configure environment

```bash
copy .env.example .env
```

Fill in:

```env
RESEND_API_KEY=re_xxxxxxxx        # from resend.com/api-keys
RESEND_FROM_EMAIL=onboarding@resend.dev   # works for testing
DIGEST_RECIPIENT_EMAIL=you@gmail.com      # must match your Resend account email
```

**Resend setup (2 minutes):**
1. Sign up at [resend.com](https://resend.com) (free)
2. Go to **API Keys** → create a key → paste into `.env`
3. Use `onboarding@resend.dev` as the sender (no domain setup required for testing)
4. Set `DIGEST_RECIPIENT_EMAIL` to the email you signed up with

### 5. Add news sources

Edit `app/collectors/sources.py` — add YouTube RSS feeds and blog URLs.

### 6. Run the pipeline

```bash
python main.py
```

## Where prompts live

All agent prompts are plain text files in `agent/prompts/`:

- **`digest_system.txt`** — tells the LLM how to behave (curator persona, output format)
- **`digest_user.txt`** — template for the user message; `{content_block}` is filled with scraped articles

Edit these files to change how the digest is generated — no code changes needed.

## Daily scheduling (free, local)

Use **Windows Task Scheduler** to run `python main.py` once a day:

1. Open Task Scheduler → Create Basic Task
2. Trigger: Daily at your preferred time
3. Action: Start a program → `C:\path\to\.venv\Scripts\python.exe C:\path\to\main.py`

## Data model

| Table | Purpose |
|-------|---------|
| `sources` | RSS feeds and blog origins |
| `content_items` | Articles and videos with full scraped text |
| `digests` | LLM-generated summaries |

## License

MIT
