# -*- coding: utf-8 -*-
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "postgresql+psycopg2://store@localhost/pgtest"
)
meta = MetaData(engine)
Base = declarative_base(metadata=meta)
session = scoped_session(sessionmaker(bind=engine))

from .store import Account, Sale, Item  # NOQA

__all__ = [
    'Account', 'Sale', 'Item',
]
