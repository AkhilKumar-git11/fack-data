from fastapi import FastAPI, Query, Header, HTTPException
from faker import Faker
from datetime import date
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import secrets


app = FastAPI()
fake = Faker()
# USAGE_LIMIT = 100  # per day limit
# usage_store = {}  # { "api_key": { "date": YYYY-MM-DD, "count": int } }

# VALID_API_KEYS = { "test123",}   # free test key
# data base added
DATABASE_URL = "sqlite:///./data.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def check_rate_limit(api_key: str):
    today = date.today().isoformat()
    db = SessionLocal()

    usage = db.query(Usage).filter(Usage.api_key == api_key).first()

    if not usage:
        usage = Usage(api_key=api_key, date=today, count=0)
        db.add(usage)

    if usage.date != today:
        usage.date = today
        usage.count = 0

    if usage.count >= 100:
        db.close()
        raise HTTPException(status_code=429, detail="Daily request limit reached")

    usage.count += 1
    db.commit()
    db.close()



def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(
        status_code=401,
        detail="API key required. Get one from /generate-key"
    )
    db = SessionLocal()
    key = db.query(ApiKey).filter(ApiKey.key == x_api_key).first()
    db.close()

    if not key:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


def generate_fake_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "country": fake.country()
    }

@app.get("/")
def home():
    return {
        "name": "Fake User Generator API",
        "endpoint": "/fake-user",
        "auth": "x-api-key header",
        "rate_limit": "100 requests/day",
        "get_key": "/generate-key"
    }

@app.post("/generate-key")
def generate_key():
    db = SessionLocal()
    key = secrets.token_hex(16)
    db.add(ApiKey(key=key))
    db.commit()
    db.close()
    return {"api_key": key}

@app.get("/fake-user")
def fake_user(
    seed: int = Query(None),
    x_api_key: str = Header(None)
):
    verify_api_key(x_api_key)
    check_rate_limit(x_api_key)

    if seed is not None:
        fake.seed_instance(seed)

    return generate_fake_user()


class ApiKey(Base):
    __tablename__ = "api_keys"
    key = Column(String, primary_key=True)

class Usage(Base):
    __tablename__ = "usage"
    api_key = Column(String, primary_key=True)
    date = Column(String)
    count = Column(Integer)

Base.metadata.create_all(bind=engine)



