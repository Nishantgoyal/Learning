# Create Engine
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# Create metadata oject
metadata_obj = MetaData()

# Create User Table
user_table = Table(
    "user_account",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String)
)

# Create Address Table With Foreign Key Constraint
address_table = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user_account.id"), nullable=False),
    Column("email_address", String, nullable=False)
)

metadata_obj.create_all(engine)
