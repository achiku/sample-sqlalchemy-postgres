"""sale partition

Revision ID: a0e862cd60ea
Revises: 6d4f2297bbf6
Create Date: 2016-06-26 17:45:34.897827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0e862cd60ea'
down_revision = '6d4f2297bbf6'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
    CREATE TABLE sale_201608 (
        CHECK (sold_at >= '2016-08-01' AND sold_at < '2016-09-01')
    ) INHERITS (sale);

    CREATE TABLE sale_201609 (
        CHECK (sold_at >= '2016-09-01' AND sold_at < '2016-10-01')
    ) INHERITS (sale);

    CREATE TABLE sale_201610 (
        CHECK (sold_at >= '2016-10-01' AND sold_at < '2016-11-01')
    ) INHERITS (sale);

    CREATE OR REPLACE FUNCTION sale_insert_trigger()
    RETURNS TRIGGER AS $$

    BEGIN
    IF (NEW.sold_at >= '2016-08-01' AND NEW.sold_at < '2016-09-01') THEN
        INSERT INTO sale_201608 VALUES (NEW.*);
    ELSIF (NEW.sold_at >= '2016-09-01' AND NEW.sold_at < '2016-10-01') THEN
        INSERT INTO sale_201609 VALUES (NEW.*);
    ELSIF (NEW.sold_at >= '2016-10-01' AND NEW.sold_at < '2016-11-01') THEN
        INSERT INTO sale_201610 VALUES (NEW.*);
    ELSE
        RAISE EXCEPTION 'Date out of range. Fix the sale_insert_trigger() function.';
    END IF;

    RETURN NULL;
    END;
    $$
    LANGUAGE plpgsql;

    CREATE TRIGGER insert_sale_trigger
        BEFORE INSERT ON sale
        FOR EACH ROW EXECUTE PROCEDURE sale_insert_trigger();
        """)


def downgrade():
    op.execute(
        """
    DROP TABLE sale_201608 ;

    DROP TABLE sale_201609 ;

    DROP TABLE sale_201610 ;

    DROP TRIGGER insert_sale_trigger ON sale ;

    DROP FUNCTION sale_insert_trigger() ;
        """
    )
    pass
