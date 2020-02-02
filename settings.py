from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

from dotenv import load_dotenv

load_dotenv()

primary_user = os.environ.get("PRIMARY_DATABASE_USER")
primary_password = os.environ.get("PRIMARY_DATABASE_PASSWORD")
primary_host = os.environ.get("PRIMARY_DATABASE_HOST")
primary_shcema = os.environ.get("PRIMARY_DATABASE_SCHEMA")
primary_connect_info = "mysql+mysqldb://{}:{}@{}:3306/{}?charset=utf8".format(
    primary_user, primary_password, primary_host, primary_shcema
)

engine = create_engine(primary_connect_info, encoding="utf-8")
read_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))

Base = declarative_base()

secondary_user = os.environ.get("SECONDARY_DATABASE_USER")
secondary_password = os.environ.get("SECONDARY_DATABASE_PASSWORD")
secondary_host = os.environ.get("SECONDARY_DATABASE_HOST")
secondary_shcema = os.environ.get("SECONDARY_DATABASE_SCHEMA")
secondary_connect_info = "mysql+mysqldb://{}:{}@{}:3306/{}?charset=utf8".format(
    secondary_user, secondary_password, secondary_host, secondary_shcema
)

write_engine = create_engine(secondary_connect_info, encoding="utf-8")
write_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=write_engine))
