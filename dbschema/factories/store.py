# -*- coding: utf-8 -*-
import random

import factory
from factory.alchemy import SQLAlchemyModelFactory

from models import session, store


class AccountFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.Account
        sqlalchemy_session = session

    email = factory.Faker('email', locale='ja_JP')
    phone_number = factory.Faker('phone_number', locale='ja_JP')


class ItemFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.Item
        sqlalchemy_session = session

    name = factory.Sequence(lambda n: 'item %03d' % n)
    price = factory.LazyAttribute(lambda n: random.randint(1000, 10000))
    description = factory.Sequence(lambda n: 'item %03d description' % n)


class SaleFactory(SQLAlchemyModelFactory):
    class Meta:
        model = store.Sale
        sqlalchemy_session = session

    account = factory.SubFactory(AccountFactory)
    item = factory.SubFactory(ItemFactory)
    paid_amount = factory.LazyAttribute(lambda n: random.randint(1000, 10000))
    sold_at = factory.Faker('date_time_this_decade')
