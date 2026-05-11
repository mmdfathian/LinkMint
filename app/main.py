from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import URLMap
from .schemas import URLCreate, URLInfo
from .utils import generate_short_code

Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener API")


@app.get("/")
def read_root():
    return {"message": "URL Shortener API is running"}


@app.post("/shorten", response_model=URLInfo)
def shorten_url(payload: URLCreate, request: Request, db: Session = Depends(get_db)):
    original_url = str(payload.url)

    short_code = generate_short_code()

    existing = db.query(URLMap).filter(URLMap.short_code == short_code).first()
    while existing:
        short_code = generate_short_code()
        existing = db.query(URLMap).filter(URLMap.short_code == short_code).first()

    new_url = URLMap(
        original_url=original_url,
        short_code=short_code,
        clicks=0
    )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    short_url = str(request.base_url) + short_code

    return URLInfo(
        id=new_url.id,
        original_url=new_url.original_url,
        short_code=new_url.short_code,
        clicks=new_url.clicks,
        created_at=new_url.created_at,
        short_url=short_url
    )


@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    url_entry = db.query(URLMap).filter(URLMap.short_code == short_code).first()

    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")

    url_entry.clicks += 1
    db.commit()

    return RedirectResponse(url=url_entry.original_url)


@app.get("/info/{short_code}", response_model=URLInfo)
def get_url_info(short_code: str, request: Request, db: Session = Depends(get_db)):
    url_entry = db.query(URLMap).filter(URLMap.short_code == short_code).first()

    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")

    short_url = str(request.base_url) + short_code

    return URLInfo(
        id=url_entry.id,
        original_url=url_entry.original_url,
        short_code=url_entry.short_code,
        clicks=url_entry.clicks,
        created_at=url_entry.created_at,
        short_url=short_url
    )

