# sample-sqlalchemy-postgres-partition
Sample setup for Postgres partitioning with SQLAlchemy

```
CREATE USER pgtest;
ALTER USER pgtest CREATEDB;
ALTER USER pgtest CREATEUSER;
-- login as pgtest
CREATE DATABASE pgtest OWNER pgtest;
CREATE USER store;
CREATE SCHEMA store AUTHORIZATION store;
```

```
$ pgpart rangep create --parent-name sale --partition-key sold_at --start-month 201608 --end-month 201611
$ pgpart rangep drop --parent-name sale --partition-key sold_at --start-month 201608 --end-month 201611
```
