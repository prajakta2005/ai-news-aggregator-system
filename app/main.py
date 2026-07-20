"""
FastAPI application entrypoint.

For Phase 1 this only proves the config → DB → app chain works.
Real routes get added from Phase 2 onward.
"""

import logging

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.config.settings import get_settings
from app.database.session import get_db
from app.utils.logging import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

settings = get_settings()

app = FastAPI(title="AI News Aggregator", version="0.1.0")


@app.get("/health")
def health_check(db: Session = Depends(get_db)) -> dict:
    """
    Confirms the app is up AND the DB connection actually works —
    a bare 200 OK that doesn't touch the DB can hide a broken connection
    until the scheduler fails at 3am.
    """
    db.execute(text("SELECT 1"))
    return {"status": "ok", "environment": settings.app_env}