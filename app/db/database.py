"""
Declarative base for all ORM models.

Kept in its own tiny module (rather than inside session.py or a models
file) so that models/*.py can import Base without ever importing the
engine/session machinery — avoids circular imports once models,
repositories, and session all reference each other.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass