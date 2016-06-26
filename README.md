# sample-sqlalchemy-postgres-partition
Sample setup for Postgres partitioning with SQLAlchemy

```
CREATE DATABASE pgtest;
CREATE SCHEMA AUTHORIZATION pgparttest;
```

```
$ pgpart rangep create --parent-name sale --partition-key sold_at --start-month 201608 --end-month 201611
$ pgpart rangep drop --parent-name sale --partition-key sold_at --start-month 201608 --end-month 201611
```
