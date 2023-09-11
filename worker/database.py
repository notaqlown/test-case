from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:password@postgres:5432/mydatabase"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'
    id = Column(String, primary_key=True)
    cadastre = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    calc = Column(Boolean)


#Base.metadata.create_all(engine)
