# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import BIGINT, TEXT
from sqlalchemy.orm import backref, relationship

from . import Base


class Account(Base):

    __tablename__ = 'account'

    id = Column(BIGINT, primary_key=True)
    email = Column(TEXT, nullable=False)
    phone_number = Column(TEXT, nullable=False)


class Item(Base):

    __tablename__ = 'item'

    id = Column(BIGINT, primary_key=True)
    name = Column(TEXT, nullable=False)
    price = Column(Integer, nullable=True)
    description = Column(String(), nullable=True)


class Sale(Base):

    __tablename__ = 'sale'

    id = Column(BIGINT, primary_key=True)
    account_id = Column(BIGINT, ForeignKey('account.id'), nullable=False)
    item_id = Column(BIGINT, ForeignKey('item.id'), nullable=False)
    paid_amount = Column(Integer, nullable=False)
    sold_at = Column(DateTime(timezone=True), nullable=False)

    account = relationship('Account', backref=backref('sales'))
    item = relationship('Item', backref=backref('item'))

    __mapper_args__ = {'polymorphic_on': sold_at}
    __table_args__ = {'implicit_returning': False}


class Sale201601(Sale):
    __tablename__ = None
    __mapper_args__ = {'polymorphic_identity': datetime.datetime(2016, 1, 1)}


class Sale201602(Sale):
    __tablename__ = None
    __mapper_args__ = {'polymorphic_identity': datetime.datetime(2016, 1, 2)}
