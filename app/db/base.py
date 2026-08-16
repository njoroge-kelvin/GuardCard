from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

# Explicit naming convention for constraints/indexes so every constraint gets
# a deterministic, predictable name instead of a DB-generated one. This
# matters for two reasons:
#   1. Alembic autogenerate needs stable names to reliably detect renames vs.
#      drop+create when diffing schemas.
#   2. Auditors/DBAs can identify exactly which table+column(s) a constraint
#      covers from its name alone, without inspecting the schema — important
#      for compliance reviews and incident debugging.
#
# Token reference:
#   %(table_name)s      - table the constraint belongs to
#   %(column_0_name)s   - first (or only) column involved
#   %(referred_table_name)s - target table for foreign keys
NAMING_CONVENTION = {
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    """Base class for all ORM models. Import this in every model module
    so Alembic's autogenerate can discover the tables via Base.metadata."""

    metadata = MetaData(naming_convention=NAMING_CONVENTION)


# Import all model modules here so they register on Base.metadata and
# Alembic autogenerate can see them, e.g.:
# from app.models.user import User  # noqa: F401