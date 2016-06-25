# -*- coding: utf-8 -*-
import random

from models import session
from factories import store

if __name__ == '__main__':
    store.ItemFactory.create_batch(size=10)
    accounts = store.AccountFactory.create_batch(size=10)
    for account in accounts:
        sale_size = random.randint(1, 3)
        store.SaleFactory.create_batch(account=account, size=sale_size)
    session.commit()
